import argparse
import os
import subprocess
import sys
from typing import Any, Optional

import requests
from llama_index.core import Settings, VectorStoreIndex
from llama_index.core.agent.runner.base import AgentRunner
from llama_index.core.indices import EmptyIndex
from llama_index.core.indices.base import BaseIndex
from llama_index.core.tools import FunctionTool
from llama_index.core.vector_stores.types import VectorStore
from rich.console import Console
from rich.markdown import Markdown
from yaspin import yaspin
from yaspin.spinners import Spinners

from atlas_talk.config import Config
from atlas_talk.settings import model, vector_store


def _index(vs: VectorStore) -> VectorStoreIndex:
    return VectorStoreIndex.from_vector_store(vs)


def _setup_index(config: Config) -> BaseIndex:
    if config.skip_rag:
        return EmptyIndex()

    if not os.path.exists(config.index_path):
        raise RuntimeError(f'index "{config.index_path}" not found, perhaps run "make prepare"')

    return _index(vector_store(config))


def _fetch_docs(input: str, *args: Any, **kwargs: Any) -> str:
    """
    Provides information about many things MongoDB, MongoDB Atlas, Drivers, atlascli.
    Use a detailed plain text question as input to the tool.

    Args:
        input : str
            Question to be answered by the tool.

    Returns:
        str
            Answer to the question in plain text.
    """
    res = requests.post(
        "https://knowledge.mongodb.com/api/v1/conversations",
        headers={
            "Origin": "https://www.mongodb.com/",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        },
    )
    if not res.ok:
        raise RuntimeError("failed to fetch docs")

    conversation = res.json()

    res = requests.post(
        f"https://knowledge.mongodb.com/api/v1/conversations/{conversation['_id']}/messages",
        json={"message": input},
        headers={
            "Origin": "https://www.mongodb.com/",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        },
    )

    if not res.ok:
        raise RuntimeError("failed to fetch docs")

    return res.json()["content"]


def _atlas_clusters_list(*args: Any, **kwargs: Any) -> str:
    """
    Useful to find information about MongoDB Atlas clusters, like number of clusters, cluster's name, state, number of members.

    Args:
        None

    Returns:
        str
            Text output with the clusters details.
    """
    output = subprocess.run(["atlas", "clusters", "list"], capture_output=True)
    return "Here is the list of clusters:\n" + output.stdout.decode("utf-8")


def _atlas_clusters_describe(input: str, *args: Any, **kwargs: Any) -> str:
    """
    Useful to find information about a particular MongoDB Atlas cluster, like cluster's name, state, number of members or connection string.

    Args:
        input : str
            Name of the cluster to describe.

    Returns:
        str
            Json output with the cluster details.
    """
    output = subprocess.run(
        ["atlas", "clusters", "describe", input, "-o", "json"], capture_output=True
    )
    output = output.stdout.decode("utf-8")

    return "Here is the output with the details of the cluster:\n" + output


# def _llm_describe_json(input: str, *args: Any, **kwargs: Any) -> str:
#     """
#     Useful to decribe a json into text and words.

#     Args:
#         input : str
#             JSON to describe.

#     Returns:
#         str
#             Details of the json in text form.
#     """
#     output = Settings.llm.complete(
#         f"""Give me a description of this json object, make sure to include details and the value of all keys in your description:
# {input}
# """
#     )
#     return output.text


def setup(config: Config) -> AgentRunner:
    """
    Set up the chat engine with the given configuration.

    This function prepares the model and index based on the provided
    configuration. It first calls `model(config)` to set up the model,
    then it uses the result of `_setup_index` to create a BaseIndex
    instance, which is finally converted to a BaseChatEngine instance
    using the system prompt from the configuration.

    Args:
        config: The configuration object that specifies how to
            set up the chat engine.

    Returns:
        A BaseChatEngine instance that is ready for use.
    """
    model(config)

    # index = _setup_index(config)

    query_engine_tools = [
        # QueryEngineTool(
        #     query_engine=index.as_query_engine(),
        #     metadata=ToolMetadata(
        #         name="cli",
        #         description="Provides information about MongoDB Atlas CLI (atlascli). Useful for retrieving information about commands and flags. "
        #         "Use a detailed plain text question as input to the tool."
        #         "Try this tool first, then try the other tools if you don't get an answer.",
        #     ),
        # ),
        FunctionTool.from_defaults(_fetch_docs),
        FunctionTool.from_defaults(_atlas_clusters_list),
        FunctionTool.from_defaults(_atlas_clusters_describe),
        # FunctionTool.from_defaults(_llm_describe_json),
    ]

    agent = AgentRunner.from_llm(
        tools=query_engine_tools, system_prompt=config.system_prompt, verbose=True
    )

    return agent


def invoke(agent: AgentRunner, prompt: str) -> str:
    """Invoke the chat engine to respond to a given prompt.

    Args:
        chat_engine: The chat engine instance.
        prompt: The input prompt to be processed by the chat engine.

    Returns:
        The response from the chat engine.
    """
    resp = agent.chat(prompt)
    return resp.response


def _repl(agent: AgentRunner, console: Console = Console(), prompt: Optional[str] = None) -> None:
    """
    Start a REPL (Read-Eval-Print Loop) session with the given chat engine.

    This function runs an interactive shell where you can type in prompts,
    and the AI chat engine will respond accordingly. To end the session, type "/bye".

    Args:
        chat_engine: The BaseChatEngine instance to use for the REPL.
        console: The rich.console.Console object to use for printing output.
        prompt: An optional initial prompt to display in the shell.
    """
    console.print(
        """Hello! How can I assist you today?

Note: type '/bye' anytime to end the chat"""
    )
    final_msg = """Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!"""
    try:
        if prompt is not None and prompt.strip() != "":
            console.print("> " + prompt)
            with yaspin(Spinners.line, color="cyan"):
                output = invoke(agent, prompt)
            console.print(Markdown(output))
        while True:
            prompt = console.input("> ")
            if prompt == "/bye":
                console.print(Markdown(final_msg))
                break
            with yaspin(Spinners.line, color="cyan"):
                output = invoke(agent, prompt)
            console.print(Markdown(output))
    except KeyboardInterrupt:
        console.print(Markdown(final_msg))
        sys.exit(130)


def run(env: Optional[str], prompt: Optional[str], skip_repl: bool = False) -> None:
    """
    Run the Atlas Talk system with the given environment and initial prompt.

    If `skip_repl` is True, it will not start a REPL session after setting up the chat engine.
    Instead, it will simply print out the response to the initial prompt (if provided).

    Args:
        env: The environment string that specifies how to set up the system.
        prompt: An optional initial prompt to display in the shell.
        skip_repl: A boolean flag indicating whether to start a REPL session or not.

    Returns:
        None
    """
    config = Config(env)

    agent = setup(config)
    console = Console()

    if skip_repl:
        if prompt is not None and prompt.strip() != "":
            output = invoke(agent, prompt)
            console.print(Markdown(output))
        return

    _repl(agent=agent, console=console, prompt=prompt)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="atlas-talk", description="interactive help of atlascli")

    parser.add_argument("--env", type=str, help="env to use")

    parser.add_argument("--prompt", type=str, help="send initial prompt")

    parser.add_argument(
        "--skip-repl",
        type=bool,
        action=argparse.BooleanOptionalAction,
        help="skip repl session",
        default=False,
    )

    args = parser.parse_args()
    run(env=args.env, prompt=args.prompt, skip_repl=args.skip_repl)

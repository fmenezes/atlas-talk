"""
atlas_talk.py

This is the main entry point for the Atlas Talk system. It provides a command-line interface (CLI) to interact with an AI chat engine.
"""

import subprocess
import os
import sys
from typing import Optional, Any

import requests
from llama_index.core import VectorStoreIndex
from llama_index.core.tools import FunctionTool, QueryEngineTool
from llama_index.core.agent.runner.base import AgentRunner
from llama_index.core.indices.base import BaseIndex
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
        f"https://knowledge.mongodb.com/api/v1/conversations/{
            conversation['_id']}/messages",
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


def setup(config: Config, verbose: bool = False) -> AgentRunner:
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


    query_engine_tools = []

    if not config.skip_rag:
        index = _setup_index(config)
        rag_tool = QueryEngineTool.from_defaults(index.as_query_engine(
        ), description='Atlas CLI Documentation.\nUseful for checking commands and their syntax.')
        query_engine_tools.append(rag_tool)

    if not config.skip_docs:
        query_engine_tools.append(FunctionTool.from_defaults(_fetch_docs))

    if not config.skip_atlascli_tools:
        query_engine_tools.append(
            FunctionTool.from_defaults(_atlas_clusters_list))
        query_engine_tools.append(
            FunctionTool.from_defaults(_atlas_clusters_describe))

    agent = AgentRunner.from_llm(
        tools=query_engine_tools, system_prompt=config.system_prompt, verbose=verbose
    )

    return agent


def invoke(agent: AgentRunner, prompt: str) -> str:
    """Invoke the chat engine to respond to a given prompt.

    Args:
        agent: The chat engine instance.
        prompt: The input prompt to be processed by the chat engine.

    Returns:
        The response from the chat engine.
    """
    resp = agent.chat(prompt)
    return resp.response


def _repl(
    agent: AgentRunner, console: Console = Console(), prompt: Optional[str] = None
) -> None:
    """
    Start a REPL (Read-Eval-Print Loop) session with the given chat engine.

    This function runs an interactive shell where you can type in prompts,
    and the AI chat engine will respond accordingly. To end the session, type "/bye".

    Args:
        agent: The AgentRunner instance to use for the REPL.
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


def run(env: Optional[str], prompt: Optional[str], skip_repl: bool = False, verbose: bool = False) -> None:
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

    agent = setup(config, verbose)
    console = Console()

    if skip_repl:
        if prompt is not None and prompt.strip() != "":
            output = invoke(agent, prompt)
            console.print(Markdown(output))
        return

    _repl(agent=agent, console=console, prompt=prompt)

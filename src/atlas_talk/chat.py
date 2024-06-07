"""
atlas_talk.py

This is the main entry point for the Atlas Talk system. It provides a command-line interface (CLI) to interact with an AI chat engine.
"""

import os
import sys
from typing import Optional

from llama_index.core import VectorStoreIndex
from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core.indices import EmptyIndex
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
    if config.skip_rag:
        return EmptyIndex()

    if not os.path.exists(config.index_path):
        raise RuntimeError(f'index "{config.index_path}" not found, perhaps run "make prepare"')

    return _index(vector_store(config))


def setup(config: Config) -> BaseChatEngine:
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

    return _setup_index(config).as_chat_engine(system_prompt=config.system_prompt)


def invoke(chat_engine: BaseChatEngine, prompt: str) -> str:
    """Invoke the chat engine to respond to a given prompt.

    Args:
        chat_engine: The chat engine instance.
        prompt: The input prompt to be processed by the chat engine.

    Returns:
        The response from the chat engine.
    """
    resp = chat_engine.chat(prompt)
    return resp.response


def _repl(
    chat_engine: BaseChatEngine, console: Console = Console(), prompt: Optional[str] = None
) -> None:
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
                output = invoke(chat_engine, prompt)
            console.print(Markdown(output))
        while True:
            prompt = console.input("> ")
            if prompt == "/bye":
                console.print(Markdown(final_msg))
                break
            with yaspin(Spinners.line, color="cyan"):
                output = invoke(chat_engine, prompt)
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

    chat_engine = setup(config)
    console = Console()

    if skip_repl:
        if prompt is not None and prompt.strip() != "":
            output = invoke(chat_engine, prompt)
            console.print(Markdown(output))
        return

    _repl(chat_engine=chat_engine, console=console, prompt=prompt)

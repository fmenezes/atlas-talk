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
    model(config)

    return _setup_index(config).as_chat_engine(system_prompt=config.system_prompt)


def invoke(chat_engine: BaseChatEngine, prompt: str) -> str:
    resp = chat_engine.chat(prompt)
    return resp.response


def _repl(
    chat_engine: BaseChatEngine, console: Console = Console(), prompt: Optional[str] = None
) -> None:
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
    config = Config(env)

    chat_engine = setup(config)
    console = Console()

    if skip_repl:
        if prompt is not None and prompt.strip() != "":
            output = invoke(chat_engine, prompt)
            console.print(Markdown(output))
        return

    _repl(chat_engine=chat_engine, console=console, prompt=prompt)

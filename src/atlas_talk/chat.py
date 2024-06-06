import os

from rich.console import Console
from rich.markdown import Markdown
from llama_index.core import VectorStoreIndex
from llama_index.core.indices import EmptyIndex
from llama_index.core.vector_stores.types import VectorStore
from llama_index.core.chat_engine.types import BaseChatEngine

from atlas_talk import set_settings, vector_store
from atlas_talk.config import Config

def index(vs: VectorStore) -> VectorStoreIndex:
    return VectorStoreIndex.from_vector_store(vs)


def setup() -> BaseChatEngine:
    set_settings()

    if Config.SKIP_RAG:
        return EmptyIndex().as_chat_engine(system_prompt=Config.SYSTEM_PROMPT)

    if not os.path.exists(Config.INDEX_PATH):
        raise RuntimeError(f'index "{Config.INDEX_PATH}" not found, perhaps run "make prepare"')

    cli_commands_index = index(vector_store())

    return cli_commands_index.as_chat_engine(system_prompt=Config.SYSTEM_PROMPT)


def invoke(chat_engine: BaseChatEngine, prompt: str) -> str:
    resp = chat_engine.chat(prompt)
    return resp.response


def repl(chat_engine: BaseChatEngine) -> None:
    console = Console()
    console.print("""Hello! How can I assist you today?

Note: type '/bye' anytime to end the chat""")
    final_msg = """Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!"""
    while True:
        try:
            prompt = input("> ")
            if prompt == "/bye":
                console.print(Markdown(final_msg))
                break
            output = invoke(chat_engine, prompt)
            console.print(Markdown(output))
        except KeyboardInterrupt:
            console.print(Markdown(final_msg))
            exit(130)


def execute(prompt: str = None) -> None:
    chat_engine = setup()

    if prompt is not None:
        output = invoke(chat_engine, prompt)
        console = Console()
        console.print(Markdown(output))
        return

    repl(chat_engine)


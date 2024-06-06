import os
import argparse

from rich.console import Console
from rich.markdown import Markdown
from llama_index.core import VectorStoreIndex
from llama_index.core.vector_stores.types import VectorStore
from llama_index.core.chat_engine.types import BaseChatEngine
from dotenv import load_dotenv

from common import set_settings, vector_store, index_path

def index(vs: VectorStore) -> VectorStoreIndex:
    return VectorStoreIndex.from_vector_store(vs)


def setup() -> BaseChatEngine:
    set_settings()

    if not os.path.exists(index_path()):
        print(f'index "{index_path()}" not found, perhaps run "make prepare"')
        exit(1)

    cli_commands_index = index(vector_store())

    return cli_commands_index.as_chat_engine(system_prompt="You are MongoDB Atlas CLI Help Assistant, you know atlas cli command reference. You should assume atlas cli is properly installed. When you don't know the answer try looking up the information first and if you still can't find it say you don't know it, do not try to make up an answer. Format your answers in Markdown.")


def invoke(chat_engine: BaseChatEngine, prompt: str) -> str:
    resp = chat_engine.chat(prompt)

    sources = list(set([f"- {node.metadata['URL']}"
                        for node in resp.source_nodes if node.metadata.get('URL')]))
    if not sources:
        return resp.response
    else:
        return f"""{resp.response}

See also:
{'\n'.join(sources)}
"""


def repl(chat_engine: BaseChatEngine) -> None:
    console = Console()
    console.print("""Hello! How can I assist you today?

Note: type '/bye' anytime to end the chat""")

    while True:
        try:
            prompt = input("> ")
            if prompt == "/bye":
                console.print(Markdown(
                    """Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!"""))
                break
            output = invoke(chat_engine, prompt)
            console.print(Markdown(output))
        except KeyboardInterrupt:
            console.print(Markdown(
                """Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!"""))
            exit(130)


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='atlas-talk',
        description='interactive help of atlascli')
    parser.add_argument('--ask', type=str)
    args = parser.parse_args()

    load_dotenv()

    chat_engine = setup()

    if args.ask:
        prompt = args.ask
        output = invoke(chat_engine, prompt)
        console = Console()
        console.print(Markdown(output))
        return

    repl(chat_engine)


if __name__ == "__main__":
    main()

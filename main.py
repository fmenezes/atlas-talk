import argparse
import uuid

from rich.console import Console
from rich.markdown import Markdown
from langchain_core.runnables.history import RunnableWithMessageHistory

from src.index import save_index
from src.chain import chain, invoke
from src import INDEX_PATH

def run_saveindex(args):
    save_index(INDEX_PATH)


def run_chat(args):
    session_id = str(uuid.uuid1())
    c = chain()
    console = Console()
    while True:
        prompt = input("> ")
        if prompt == "/bye":
            exit()
        output = invoke(c, session_id, prompt)
        console.print(Markdown(output))


parser = argparse.ArgumentParser(prog='atlas-talk')
subparsers = parser.add_subparsers()

saveindex = subparsers.add_parser('save-index')
saveindex.set_defaults(func=run_saveindex)
chat = subparsers.add_parser('chat')
chat.set_defaults(func=run_chat)

args = parser.parse_args()
args.func(args)

import argparse

from src.chat import run_chat

parser = argparse.ArgumentParser(prog='atlas-talk')
subparsers = parser.add_subparsers()

chat = subparsers.add_parser('chat')
chat.set_defaults(func=run_chat)

args = parser.parse_args()
args.func(args)

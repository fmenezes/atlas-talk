import argparse
from atlas_talk.commands import prepare, chat


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='atlas-talk',
        description='interactive help of atlascli')

    subparsers = parser.add_subparsers(dest='command')

    parser_chat = subparsers.add_parser(
        'chat', help='initiate a chat session')
    parser_chat.add_argument(
        '--ask', type=str, help='send prompt without repl session')
    parser_chat.set_defaults(func=chat.execute)


    parser_prepare = subparsers.add_parser(
        'prepare', help='prepare index for chat')
    parser_prepare.set_defaults(func=prepare.execute)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

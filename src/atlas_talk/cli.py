import argparse
from atlas_talk.chat import execute

def main() -> None:
    parser = argparse.ArgumentParser(
        prog='atlas-talk',
        description='interactive help of atlascli')

    parser.add_argument(
        '--ask', type=str, help='send prompt without repl session')

    args = parser.parse_args()
    execute(prompt=args.ask)

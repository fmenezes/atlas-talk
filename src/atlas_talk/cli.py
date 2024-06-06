import argparse
from atlas_talk.chat import run


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="atlas-talk", description="interactive help of atlascli"
    )

    parser.add_argument("--env", type=str, help="env to use", default="default")

    parser.add_argument("--ask", type=str, help="send prompt without repl session")

    args = parser.parse_args()
    run(env=args.env, prompt=args.ask)

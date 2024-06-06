import argparse

from atlas_talk.chat import run


def main() -> None:
    parser = argparse.ArgumentParser(prog="atlas-talk", description="interactive help of atlascli")

    parser.add_argument("--env", type=str, help="env to use")

    parser.add_argument("--prompt", type=str, help="send initial prompt")

    parser.add_argument(
        "--skip-repl",
        type=bool,
        action=argparse.BooleanOptionalAction,
        help="skip repl session",
        default=False,
    )

    args = parser.parse_args()
    run(env=args.env, prompt=args.prompt, skip_repl=args.skip_repl)

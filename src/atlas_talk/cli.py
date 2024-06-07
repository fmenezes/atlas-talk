"""
atlas-talk: Interactive Help of atlascli
==============================================

This is the main entry point for the atlas-talk program.
The atlas-talk provides interactive help for users by allowing them to talk with a bot or ask questions and receive answers.
This module handles command line arguments, parsing them using argparse, and then calling the run function from the atlas_talk.chat import run.
"""

import argparse

from atlas_talk.chat import run


def main() -> None:
    """
    Entry point for the atlas-talk program.

    Args:
        --env str: The environment to use.
        --prompt str: Send an initial prompt.
        --skip-repl bool (optional): Skip REPL session. Defaults to False.

    Returns:
        None
    """
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

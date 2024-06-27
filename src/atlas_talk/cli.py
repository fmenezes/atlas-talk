"""
atlas-talk: Interactive Help of atlascli
==============================================

This is the main entry point for the atlas-talk program.
The atlas-talk provides interactive help for users by allowing them to talk with a bot or ask questions and receive answers.
This module handles command line arguments, parsing them using argparse, and then calling the run function from the atlas_talk.chat import run.
"""

import argparse
import sys
from typing import Optional

import requests
from yaspin import yaspin
from yaspin.spinners import Spinners
from rich.console import Console
from rich.markdown import Markdown

def _invoke(prompt: str) -> str:
    url = "http://127.0.0.1:5000/conversation"
    data = {
        "prompt": prompt
    }
    response = requests.post(url, json=data)
    response.raise_for_status()
    j = response.json()
    return j['response']


def _repl(console: Console = Console(), prompt: Optional[str] = None) -> None:
    """
    Start a REPL (Read-Eval-Print Loop) session with the given chat engine.

    This function runs an interactive shell where you can type in prompts,
    and the AI chat engine will respond accordingly. To end the session, type "/bye".

    Args:
        agent: The AgentRunner instance to use for the REPL.
        console: The rich.console.Console object to use for printing output.
        prompt: An optional initial prompt to display in the shell.
    """
    console.print(
        """Hello! How can I assist you today?

Note: type '/bye' anytime to end the chat"""
    )
    final_msg = """Goodbye! If you have any more questions in the future, feel free to ask. Have a great day!"""
    try:
        if prompt is not None and prompt.strip() != "":
            console.print("> " + prompt)
            with yaspin(Spinners.line, color="cyan"):
                output = _invoke(prompt)
            console.print(Markdown(output))
        while True:
            prompt = console.input("> ")
            if prompt == "/bye":
                console.print(Markdown(final_msg))
                break
            with yaspin(Spinners.line, color="cyan"):
                output = _invoke(prompt)
            console.print(Markdown(output))
    except KeyboardInterrupt:
        console.print(Markdown(final_msg))
        sys.exit(130)


def _run(
    env: Optional[str], prompt: Optional[str], skip_repl: bool = False, verbose: bool = False
) -> None:
    """
    Run the Atlas Talk system with the given environment and initial prompt.

    If `skip_repl` is True, it will not start a REPL session after setting up the chat engine.
    Instead, it will simply print out the response to the initial prompt (if provided).

    Args:
        env: The environment string that specifies how to set up the system.
        prompt: An optional initial prompt to display in the shell.
        skip_repl: A boolean flag indicating whether to start a REPL session or not.

    Returns:
        None
    """
    console = Console()

    if skip_repl:
        if prompt is not None and prompt.strip() != "":
            output = _invoke(prompt)
            console.print(Markdown(output))
        return

    _repl(console=console, prompt=prompt)


def main() -> None:
    """
    Entry point for the atlas-talk program.

    Args:
        --env str: The environment to use.
        --prompt str: Send an initial prompt.
        --skip-repl bool (optional): Skip REPL session. Defaults to False.
        --verbose bool (optional): Skip REPL session. Defaults to False.

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

    parser.add_argument(
        "--verbose",
        type=bool,
        action=argparse.BooleanOptionalAction,
        help="verbose output",
        default=False,
    )

    args = parser.parse_args()
    _run(env=args.env, prompt=args.prompt, skip_repl=args.skip_repl, verbose=args.verbose)

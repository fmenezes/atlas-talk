import argparse

from flask import Flask, jsonify, request
from llama_index.core.agent.runner.base import AgentRunner

from atlas_talk.chat import invoke, setup
from atlas_talk.config import Config

app = Flask(__name__)
config: Config = None
agent: AgentRunner = None


@app.route("/", methods=["GET"])
def _index():
    return jsonify({"response": "OK"}), 200


@app.route("/conversation", methods=["POST"])
def _conversation():
    data = request.get_json()
    if data["prompt"] is None:
        return jsonify({"error": "invalid request"}), 400
    response = invoke(agent, data["prompt"])
    return jsonify({"response": response}), 200


def _main() -> None:
    global config
    global agent

    parser = argparse.ArgumentParser(
        prog="atlas-talk", description="interactive help of atlascli")

    parser.add_argument("--env", type=str, help="env to use")
    args = parser.parse_args()
    
    config = Config(args.env)
    agent = setup(config, verbose=True)
    app.run()


if __name__ == "__main__":
    _main()

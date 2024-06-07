import pytest
import sys

from atlas_talk.config import Config
from atlas_talk.chat import setup
from llama_index.core.evaluation import RelevancyEvaluator, FaithfulnessEvaluator

prompts = ["How do I create a cluster?", "How to create an atlas search index?"]
envs = ['openai', 'openai-gpt-4o', 'ollama']
evaluators = [
    FaithfulnessEvaluator,
    RelevancyEvaluator,
]
query_env_evals = [(p, e, ev) for ev in evaluators for p in prompts for e in envs]


@pytest.mark.parametrize('query,env,evaluator_cls', query_env_evals)
def test_evaluation(query, env, evaluator_cls):
    config = Config(env)
    engine = setup(config)
    response = engine.chat(query)
    evaluator = evaluator_cls()
    result = evaluator.evaluate_response(
        query=query, response=response)
    if isinstance(result.passing, bool):
        assert result.passing, result.feedback
    else:
        pytest.skip(result.feedback)

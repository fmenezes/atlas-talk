from typing import List, Type
import os

import pytest

from atlas_talk.config import Config
from atlas_talk.settings import model
from atlas_talk.chat import setup
from llama_index.core.evaluation import RelevancyEvaluator, FaithfulnessEvaluator
from llama_index.core.evaluation.base import BaseEvaluator

def envs() -> List[str]:
    files = os.listdir('./env')
    envs = [os.path.basename(f).removesuffix('.env')
             for f in files if f.endswith('.env')]
    envs += [None]
    return envs


@pytest.mark.parametrize(
    "env",
    envs(),
)
class TestEvaluation:
    """Tests to run on each environment."""

    @pytest.fixture
    def prompts(self) -> List[str]:
        """Prompts to be tested"""
        return ["How do I create a cluster?",
                "How to create an atlas search index?"]

    def evaluate(self, evaluator_cls: Type[BaseEvaluator], env: str, prompts: List[str]) -> None:
        model(Config(None))  # setup evaluator
        evaluator = evaluator_cls()

        config = Config(env)
        engine = setup(config)
        for query in prompts:
            response = engine.chat(query)
            result = evaluator.evaluate_response(
                query=query, response=response)
            if isinstance(result.passing, bool):
                assert result.passing, result.feedback
            else:
                pytest.skip(result.feedback)

    def test_faithfulness(self, env: str, prompts: List[str]) -> None:
        self.evaluate(FaithfulnessEvaluator, env, prompts)

    def test_relevancy(self, env: str, prompts: List[str]) -> None:
        self.evaluate(RelevancyEvaluator, env, prompts)

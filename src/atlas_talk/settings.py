"""
This module provides functionality for setting up various AI models and platforms.
"""

from time import sleep
from typing import Sequence

import chromadb
from llama_index.core import Settings
from llama_index.core.base.llms.types import ChatMessage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.llama_cpp import LlamaCPP
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from llama_index.vector_stores.chroma import ChromaVectorStore
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from atlas_talk.config import Config


def _get_cookie(url: str, cookie_domain: str) -> str:
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        while True:
            cookies = driver.get_cookies()
            filter_cookies = [cookie for cookie in cookies if cookie.get("domain") == cookie_domain]
            if len(filter_cookies) > 0:
                cookie_header = "; ".join(
                    [f"{cookie['name']}={cookie['value']}" for cookie in filter_cookies]
                )
                return cookie_header
            sleep(0.5)
    except WebDriverException as e:
        raise e
    finally:
        try:
            driver.quit()
        except WebDriverException:
            pass


def _messages_to_prompt(messages: Sequence[ChatMessage]) -> str:
    """
    Convert a sequence of chat messages into a prompt.

    Args:
        messages: A sequence of ChatMessage objects.

    Returns:
        The generated prompt.
    """

    prompt = ""
    for message in messages:
        if message.role == "system":
            prompt += f"<|system|>\n{message.content}</s>\n"
        elif message.role == "user":
            prompt += f"<|user|>\n{message.content}</s>\n"
        elif message.role == "assistant":
            prompt += f"<|assistant|>\n{message.content}</s>\n"

    # ensure we start with a system prompt, insert blank if needed
    if not prompt.startswith("<|system|>\n"):
        prompt = "<|system|>\n</s>\n" + prompt

    # add final assistant prompt
    prompt = prompt + "<|assistant|>\n"

    return prompt


def _completion_to_prompt(completion: str) -> str:
    """
    Convert a completion string into a prompt.

    Args:
        completion: The generated text.

    Returns:
        The generated prompt.
    """

    return f"<|system|>\n</s>\n<|user|>\n{completion}</s>\n<|assistant|>\n"


def vector_store(config: Config):
    """
    Initialize the Chroma vector store using a given configuration.

    Args:
        config: The configuration object.
    """

    chroma_client = chromadb.PersistentClient(config.index_path)
    chroma_collection = chroma_client.get_or_create_collection(config.collection_name)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def _set_openai(config: Config) -> None:
    """
    Set the OpenAI model and embedder using a given configuration.

    Args:
        config: The configuration object.
    """

    headers = {}
    if config.cookie_url is not None and config.cookie_domain is not None:
        headers["Cookie"] = _get_cookie(config.cookie_url, config.cookie_domain)

    Settings.llm = OpenAI(
        model=config.openai_model,
        api_key=config.openai_api_key,
        api_base=config.openai_api_base_url,
        default_headers=headers,
    )
    Settings.embed_model = OpenAIEmbedding(
        model=config.openai_embed_model,
        api_key=config.openai_api_key,
        api_base=config.openai_api_base_url,
        default_headers=headers,
    )


def _set_ollama(config: Config) -> None:
    """
    Set the Ollama model and embedder using a given configuration.

    Args:
        config: The configuration object.
    """

    Settings.embed_model = OllamaEmbedding(model_name=config.ollama_embed_model)
    Settings.llm = Ollama(model=config.ollama_model, temperature=0.5)


def _set_llama_cpp(config: Config) -> None:
    """
    Set the LLaMA-CPP model and embedder using a given configuration.

    Args:
        config: The configuration object.
    """

    Settings.embed_model = HuggingFaceEmbedding(model_name=config.llama_cpp_embed_model)
    Settings.llm = LlamaCPP(
        model_url=config.llama_cpp_model_url,
        verbose=False,
        model_kwargs={"n_gpu_layers": config.n_gpu_layers},
        messages_to_prompt=_messages_to_prompt,
        completion_to_prompt=_completion_to_prompt,
    )


def model(config: Config) -> None:
    """
    Set the AI model and embedder based on a given configuration.

    Args:
        config: The configuration object.
    """

    match config.ai_platform:
        case "OLLAMA":
            _set_ollama(config)
        case "OPENAI":
            _set_openai(config)
        case "LLAMA_CPP":
            _set_llama_cpp(config)
        case _:
            raise RuntimeError(f"invalid platform: {config.ai_platform}")

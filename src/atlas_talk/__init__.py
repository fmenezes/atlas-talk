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

from atlas_talk.config import Config


def _messages_to_prompt(messages: Sequence[ChatMessage]) -> str:
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
    return f"<|system|>\n</s>\n<|user|>\n{completion}</s>\n<|assistant|>\n"


def vector_store(config: Config):
    chroma_client = chromadb.PersistentClient(config.index_path)
    chroma_collection = chroma_client.get_or_create_collection(config.collection_name)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def _set_openai(config: Config) -> None:
    Settings.embed_model = OpenAIEmbedding(model=config.openai_embed_model)
    Settings.llm = OpenAI(model=config.openai_model, api_key=config.openai_api_key)


def _set_ollama(config: Config) -> None:
    Settings.embed_model = OllamaEmbedding(model_name=config.ollama_embed_model)
    Settings.llm = Ollama(model=config.ollama_model, temperature=0.5)


def _set_llama_cpp(config: Config) -> None:
    Settings.embed_model = HuggingFaceEmbedding(model_name=config.llama_cpp_embed_model)
    Settings.llm = LlamaCPP(
        model_url=config.llama_cpp_model_url,
        verbose=False,
        model_kwargs={"n_gpu_layers": config.n_gpu_layers},
        messages_to_prompt=_messages_to_prompt,
        completion_to_prompt=_completion_to_prompt,
    )


def set_settings(config: Config) -> None:
    match config.ai_platform:
        case "OLLAMA":
            _set_ollama(config)
        case "OPENAI":
            _set_openai(config)
        case "LLAMA_CPP":
            _set_llama_cpp(config)
        case _:
            raise RuntimeError(f"invalid platform: {config.ai_platform}")

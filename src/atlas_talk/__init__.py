from typing import Sequence

from atlas_talk.config import Config
from llama_index.core import Settings
from llama_index.core.base.llms.types import ChatMessage

def _messages_to_prompt(messages: Sequence[ChatMessage]) -> str:
    prompt = ""
    for message in messages:
        if message.role == 'system':
            prompt += f"<|system|>\n{message.content}</s>\n"
        elif message.role == 'user':
            prompt += f"<|user|>\n{message.content}</s>\n"
        elif message.role == 'assistant':
            prompt += f"<|assistant|>\n{message.content}</s>\n"

    # ensure we start with a system prompt, insert blank if needed
    if not prompt.startswith("<|system|>\n"):
        prompt = "<|system|>\n</s>\n" + prompt

    # add final assistant prompt
    prompt = prompt + "<|assistant|>\n"

    return prompt


def _completion_to_prompt(completion: str) -> str:
    return f"<|system|>\n</s>\n<|user|>\n{completion}</s>\n<|assistant|>\n"


def vector_store():
    import chromadb
    from llama_index.vector_stores.chroma import ChromaVectorStore

    chroma_client = chromadb.PersistentClient(Config.INDEX_PATH)
    chroma_collection = chroma_client.get_or_create_collection(
        Config.COLLECTION_NAME)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def _set_openai() -> None:
    from llama_index.embeddings.openai import OpenAIEmbedding
    from llama_index.llms.openai import OpenAI

    Settings.embed_model = OpenAIEmbedding(
        model=Config.OPENAI_EMBED_MODEL)
    Settings.llm = OpenAI(model=Config.OPENAI_MODEL)


def _set_ollama() -> None:
    from llama_index.llms.ollama import Ollama
    from llama_index.embeddings.ollama import OllamaEmbedding

    Settings.embed_model = OllamaEmbedding(
        model_name=Config.OLLAMA_EMBED_MODEL
    )
    Settings.llm = Ollama(model=Config.OLLAMA_MODEL, temperature=0.5)


def _set_llama_cpp() -> None:
    from llama_index.llms.llama_cpp import LlamaCPP
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding

    Settings.embed_model = HuggingFaceEmbedding(
        model_name=Config.LLAMA_CPP_EMBED_MODEL
    )
    Settings.llm = LlamaCPP(
        model_url=Config.LLAMA_CPP_MODEL_URL,
        verbose=False,
        model_kwargs={'n_gpu_layers':-1},
        messages_to_prompt=_messages_to_prompt,
        completion_to_prompt=_completion_to_prompt
    )


def set_settings() -> None:
    match Config.AI_PLATFORM:
        case 'OLLAMA':
            _set_ollama()
        case 'OPENAI':
            _set_openai()
        case 'LLAMA_CPP':
            _set_llama_cpp()
        case _:
            raise RuntimeError(f"invalid platform: {Config.AI_PLATFORM}")


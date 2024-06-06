import os
from dotenv import load_dotenv

from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL
from llama_index.embeddings.openai import OpenAIEmbeddingModeModel
from llama_index.embeddings.huggingface.utils import DEFAULT_HUGGINGFACE_EMBEDDING_MODEL

ENV_FILE = f'./env/{os.environ.get('ENV', 'default')}.env'
load_dotenv(ENV_FILE, override=True)  # loads openai.env, ollama.env, etc

class Config:
    ENV_FILE: str = ENV_FILE
    SYSTEM_PROMPT: str = os.environ.get('SYSTEM_PROMPT')
    INDEX_PATH: str = os.environ.get('INDEX_PATH', './data/index')
    COLLECTION_NAME: str = os.environ.get('COLLECTION_NAME', 'atlascli-commands')
    AI_PLATFORM: str = os.environ.get('AI_PLATFORM', 'OPENAI')
    OPENAI_MODEL: str = os.environ.get('OPENAI_MODEL', DEFAULT_OPENAI_MODEL)
    OPENAI_EMBED_MODEL: str = os.environ.get(
        'OPENAI_EMBED_MODEL', OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002)
    OLLAMA_MODEL: str = os.environ.get('OLLAMA_MODEL', 'mistral')
    OLLAMA_EMBED_MODEL: str = os.environ.get(
        'OLLAMA_EMBED_MODEL', 'nomic-embed-text')
    LLAMA_CPP_MODEL_URL: str = os.environ.get('LLAMA_CPP_MODEL_URL', 'https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_0.gguf')
    LLAMA_CPP_EMBED_MODEL: str = os.environ.get(
        'LLAMA_CPP_EMBED_MODEL', DEFAULT_HUGGINGFACE_EMBEDDING_MODEL)
    SKIP_RAG: bool = os.getenv(
        "SKIP_RAG", 'False').lower() in ('true', '1', 't')

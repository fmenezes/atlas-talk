import os
from dotenv import load_dotenv

from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL
from llama_index.embeddings.openai import OpenAIEmbeddingModeModel

load_dotenv()

class Config:
    INDEX_PATH: str = os.environ.get('INDEX_PATH', './data/index')
    COLLECTION_NAME: str = os.environ.get('COLLECTION_NAME', 'atlascli-commands')
    AI_PLATFORM: str = os.environ.get('AI_PLATFORM', 'OPENAI')
    OPENAI_MODEL: str = os.environ.get('OPENAI_MODEL', DEFAULT_OPENAI_MODEL)
    OPENAI_EMBED_MODEL: str = os.environ.get(
        'OPENAI_EMBED_MODEL', OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002)
    OLLAMA_MODEL: str = os.environ.get('OLLAMA_MODEL', 'mistral')
    OLLAMA_EMBED_MODEL: str = os.environ.get(
        'OLLAMA_EMBED_MODEL', 'nomic-embed-text')

import os

from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModeModel
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

def index_path():
    return os.environ.get('INDEX_PATH', './data/index')


def vector_store():
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'atlascli-commands')

    chroma_client = chromadb.PersistentClient(index_path())
    chroma_collection = chroma_client.get_or_create_collection(COLLECTION_NAME)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def set_settings() -> None:
    AI_PLATFORM = os.environ.get('AI_PLATFORM', 'OPENAI')
    match AI_PLATFORM:
        case 'OLLAMA':
            Settings.embed_model = OllamaEmbedding(
                model_name=os.environ.get(
                    'OLLAMA_EMBED_MODEL', 'nomic-embed-text')
            )
            Settings.llm = Ollama(model=os.environ.get(
                'OLLAMA_MODEL', 'mistral'), temperature=0.5)
        case 'OPENAI':
            Settings.embed_model = OpenAIEmbedding(model=os.environ.get(
                'OPENAI_EMBED_MODEL', OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002))
            Settings.llm = OpenAI(model=os.environ.get(
                'OPENAI_MODEL', DEFAULT_OPENAI_MODEL))
        case _:
            raise RuntimeError(f"invalid platform: {AI_PLATFORM}")


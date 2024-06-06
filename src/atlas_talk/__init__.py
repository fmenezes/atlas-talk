from atlas_talk.config import Config
from llama_index.core import Settings


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


def set_settings() -> None:
    match Config.AI_PLATFORM:
        case 'OLLAMA':
            _set_ollama()
        case 'OPENAI':
            _set_openai()
        case _:
            raise RuntimeError(f"invalid platform: {Config.AI_PLATFORM}")

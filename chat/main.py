import os

from rich.console import Console
from rich.markdown import Markdown
from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.openai import OpenAI
from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModeModel
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.chat_engine.types import BaseChatEngine
import chromadb
from dotenv import load_dotenv

def set_settings() -> None:
    AI_PLATFORM = os.environ.get('AI_PLATFORM', 'OPENAI')
    if AI_PLATFORM == 'OLLAMA':
        Settings.embed_model = OllamaEmbedding(
            model_name=os.environ.get('OLLAMA_EMBED_MODEL', 'nomic-embed-text')
        )
        Settings.llm = Ollama(model=os.environ.get(
            'OLLAMA_MODEL', 'mistral'), temperature=0.5)
    elif AI_PLATFORM == 'OPENAI':
        Settings.embed_model = OpenAIEmbedding(model=os.environ.get(
            'OPENAI_EMBED_MODEL', OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002))
        Settings.llm = OpenAI(model=os.environ.get(
            'OPENAI_MODEL', DEFAULT_OPENAI_MODEL))


def vector_store(src: str, collection_name: str):
    chroma_client = chromadb.PersistentClient(src)
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def index(vs: VectorStore) -> VectorStoreIndex:
    return VectorStoreIndex.from_vector_store(vs)


def setup() -> BaseChatEngine:
    load_dotenv()

    INDEX_PATH = os.environ.get('INDEX_PATH', './data/index')
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'atlascli-commands')

    if not os.path.exists(INDEX_PATH):
        print(f'index "{INDEX_PATH}" not found, perhaps run "make prepare"')
        exit(1)

    set_settings()
    cli_commands_index = index(vector_store(INDEX_PATH, COLLECTION_NAME))

    return cli_commands_index.as_chat_engine(system_prompt="You are MongoDB Atlas CLI Help Assistant, you know atlas cli command reference. You should assume atlas cli is properly installed. When you don't know the answer say you don't know it do not try to make up an answer.")


def invoke(chat_engine: BaseChatEngine, prompt: str) -> str:
    resp = chat_engine.chat(prompt)

    sources = list(set([f"- {node.metadata['URL']}"
                        for node in resp.source_nodes if node.metadata.get('URL')]))
    if not sources:
        return resp.response
    else:
        return f"""{resp.response}

See also:
{'\n'.join(sources)}
"""


def main():
    console = Console()
    chat_engine = setup()
    prompt = os.environ.get('INIT_PROMPT')
    if prompt is not None:
        output = invoke(chat_engine, prompt)
        console.print(Markdown(output))
    else:
        console.print("Hello, how can I help?")
        console.print("")
    console.print("Note: type '/bye' anytime to end the chat")
    while True:
        prompt = input("> ")
        if prompt == "/bye":
            console.print(Markdown("""Goodbye!
Note: to check more about this project go to http://github.com/fmenezes/atlas-talk"""))
            break
        output = invoke(chat_engine, prompt)
        console.print(Markdown(output))


if __name__ == "__main__":
    main()

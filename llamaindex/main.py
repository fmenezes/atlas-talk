from typing import Sequence, Dict
import os

from rich.console import Console
from rich.markdown import Markdown
from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)

Settings.llm = Ollama(model='llama3')
Settings.embed_model = embed_model

def vector_store(src: str):
    chroma_client = chromadb.PersistentClient(src)
    chroma_collection = chroma_client.get_or_create_collection("mongodb")
    return ChromaVectorStore(chroma_collection=chroma_collection)


def index(vs: VectorStore) -> VectorStoreIndex:
    return VectorStoreIndex.from_vector_store(vs)


def engine(index: VectorStoreIndex) -> BaseChatEngine:
    return index.as_chat_engine(chat_history=[
        ChatMessage(role=MessageRole.SYSTEM, content="You are an assistant helping the user on how to use MongoDB Atlas CLI. If you don't know the answer make sure to say you don't know do not make up an answer. Format your responses in Markdown.")
    ])


def setup() -> BaseChatEngine:
    if not os.path.exists("./data/llamaindex_index"):
        print('index "./data/llamaindex_index" not found')
        exit(1)
    vs = vector_store("./data/llamaindex_index")
    
    return engine(index(vs))


def invoke(engine: BaseChatEngine, prompt: str) -> str:
    resp = engine.chat(prompt)

    return f"""{resp.response}
"""


def main():
    console = Console()
    chat_engine = setup()
    while True:
        prompt = input("> ")
        if prompt == "/bye":
            exit()
        output = invoke(chat_engine, prompt)
        console.print(Markdown(output))


if __name__ == "__main__":
    main()

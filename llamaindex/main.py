from typing import Sequence, Dict
import json

from rich.console import Console
from rich.markdown import Markdown
from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.schema import Document
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

from llamaindex.html_loader import HTMLReader

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)

Settings.llm = Ollama(model='llama3')
Settings.embed_model = embed_model

def vector_store():
    chroma_client = chromadb.EphemeralClient()
    chroma_collection = chroma_client.get_or_create_collection("mongodb")
    return ChromaVectorStore(chroma_collection=chroma_collection)


def load_metadata(p: str) -> Dict:
    mp = p.removesuffix('.html') + '_metadata.json'
    with open(mp, "r") as f:
        return json.load(f)


def load_docs() -> Sequence[Document]:
    loader = SimpleDirectoryReader(input_dir="./data/old", recursive=True, required_exts=[
                                   '.html'], file_metadata=load_metadata, file_extractor={'.html': HTMLReader})
    return loader.load_data()


def ingest(vector_store: VectorStore):
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=200, chunk_overlap=0),
            TitleExtractor(),
            embed_model,
        ],
        vector_store=vector_store,
    )
    pipeline.run(documents=load_docs())


def index(vs: VectorStore) -> VectorStoreIndex:
    return VectorStoreIndex.from_vector_store(vs)


def engine(index: VectorStoreIndex) -> BaseChatEngine:
    return index.as_chat_engine(chat_history=[
        ChatMessage(role=MessageRole.SYSTEM, content="You are an assistant helping the user on how to use MongoDB Atlas CLI. If you don't know the answer make sure to say you don't know do not make up an answer. Format your responses in Markdown.")
    ])


def setup() -> BaseChatEngine:
    vs = vector_store()
    ingest(vs)

    return engine(index(vs))


def invoke(engine: BaseChatEngine, prompt: str) -> str:
    resp = engine.chat(prompt)

    return f"""{resp.response}

### sources
{'\n'.join(set([f" - {src.metadata['URL']}" for src in resp.source_nodes]))}"""


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

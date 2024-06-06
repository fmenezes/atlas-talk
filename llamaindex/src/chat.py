from typing import Sequence, List
import os
import uuid
from urllib.parse import urlparse
from urllib.request import urlretrieve
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
from llama_index.readers.web import BeautifulSoupWebReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from bs4 import BeautifulSoup

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)

Settings.llm = Ollama(model='llama3')
Settings.embed_model = embed_model

def vector_store():
    chroma_client = chromadb.EphemeralClient()
    chroma_collection = chroma_client.get_or_create_collection("mongodb")
    return ChromaVectorStore(chroma_collection=chroma_collection)


def extract_links(url: str, file_path: str) -> List[str]:
    parsed_url = urlparse(url)
    prefix = f"{parsed_url.scheme}://{parsed_url.netloc}"

    with open(file_path) as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        raw_links = [
            a['href'] for a in soup.find_all('a', href=True)
        ]
        all_links = [
            f"{prefix}{link}" if link.startswith('/') else f"{url}{link}" if link.startswith('#') else link for link in raw_links
        ]
        links_without_anchors = [
            link.split('#')[0] for link in all_links]
        links = list(set(links_without_anchors))
        return links


def process_docs(url: str, filter: tuple[str, ...]) -> None:
    data = {
        'by_ids': {},
        'by_urls': {},
        'failed': [],
    }

    data_path = os.path.abspath(f"./data/map.json")
    if os.path.exists(data_path):
        with open(data_path, "r") as f:
            data = json.load(f)

    to_visit = [url]
    filter = tuple([url]) + filter
    already_visited = []
    while len(to_visit) > 0:
        url = to_visit.pop()
        print(f'processing {url}')
        already_visited += [url]
        id = data['by_urls'].get(url) or str(uuid.uuid4())
        p = os.path.abspath(f"./data/{id}.html")
        failed = False
        if not os.path.exists(p):
            d = os.path.dirname(p)
            os.makedirs(d, exist_ok=True)
            data['by_urls'][url] = id
            data['by_ids'][id] = url
            try:
                urlretrieve(url, p)
            except:
                data['failed'] += url
                failed = True
            with open(data_path, "w") as f:
                json.dump(data, f, indent=2)
        if failed:
            continue
        new_links = extract_links(url, p)
        new_links = [link for link in new_links if link.startswith(filter)]
        new_links = [link for link in new_links if link not in already_visited]
        to_visit += new_links


def load_docs(urls: List[str]) -> Sequence[Document]:
    loader = SimpleDirectoryReader()
    return loader.load_data(urls=urls)


def ingest(vector_store: VectorStore):
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=200, chunk_overlap=0),
            TitleExtractor(),
            embed_model,
        ],
        vector_store=vector_store,
    )
    local_path = './llamaindex/pipeline_storage'
    if (os.path.exists(local_path)):
        pipeline.load(local_path)
    else:
        process_docs("https://www.mongodb.com/docs/", (
            "http://www.mongodb.com/docs/",
            "https://mongodb.com/docs/",
            "http://mongodb.com/docs/",
            "https://docs.mongodb.com/",
            "http://docs.mongodb.com/",
        ))
        pipeline.run(documents=load_docs())
        pipeline.persist(local_path)


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


def run_chat(args):
    console = Console()
    chat_engine = setup()
    while True:
        prompt = input("> ")
        if prompt == "/bye":
            exit()
        output = invoke(chat_engine, prompt)
        console.print(Markdown(output))

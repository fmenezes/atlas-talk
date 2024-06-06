from typing import List

from urllib.parse import urlparse
import ollama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document
from langchain_community.document_loaders import AsyncChromiumLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from bs4 import BeautifulSoup

from src import EMBEDDING_MODEL

def load_docs() -> List[Document]:
    to_visit = ["https://www.mongodb.com/docs/atlas/cli/stable/"]

    already_visited = []

    docs = []

    while len(to_visit) > 0:
        print(f'processing {to_visit}')
        loader = AsyncChromiumLoader(to_visit)
        current_docs = loader.load()
        already_visited += to_visit
        links = extract_links(current_docs)
        links = [link for link in links if link.startswith(("https://www.mongodb.com/docs/atlas/cli", "http://www.mongodb.com/docs/atlas/cli", "https://mongodb.com/docs/atlas/cli", "http://www.mongodb.com/docs/atlas/cli", "https://docs.mongodb.com/atlas/cli", "http://docs.mongodb.com/atlas/cli"))]
        to_visit = [link for link in links if link not in already_visited]
        docs += current_docs

    return docs


def extract_links(docs: List[Document]) -> List[str]:
    links = []

    for doc in docs:
        url = urlparse(doc.metadata['source'])
        prefix = f"{url.scheme}://{url.netloc}"

        soup = BeautifulSoup(doc.page_content, "html.parser")
        raw_links = [
            a['href'] for a in soup.find_all('a', href=True)
        ]
        all_links = [
            f"{prefix}{link}" if link.startswith('/') else f"{doc.metadata['source']}{link}" if link.startswith('#') else link for link in raw_links
        ]
        links_without_anchors = [
            link.split('#')[0] for link in all_links]
        links += links_without_anchors

    links = list(set(links))
    return links


def html_to_markdown(docs: List[Document]) -> List[Document]:
    html2text = Html2TextTransformer()
    return html2text.transform_documents(docs)


def split_docs(docs: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter()
    return text_splitter.split_documents(docs)


def vector_store(docs: List[Document]) -> VectorStore:
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    return FAISS.from_documents(docs, embeddings)


def save_index(path: str):
    ollama.pull(EMBEDDING_MODEL)
    vector_store(split_docs(html_to_markdown(load_docs()))).save_local(path)


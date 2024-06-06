from typing import List
import os
from urllib.parse import urlparse

from shutil import rmtree
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

def save_index(dest: str):
    process(dest, "https://www.mongodb.com/docs/atlas/", (
        "https://www.mongodb.com/docs/atlas/",
        "http://www.mongodb.com/docs/atlas/",
        "https://mongodb.com/docs/atlas/",
        "http://mongodb.com/docs/atlas/",
        "https://docs.mongodb.com/atlas/",
        "http://docs.mongodb.com/atlas/"
    ))

 
def process(dest: str, url: str, filter: tuple[str, ...]):
    ollama.pull(EMBEDDING_MODEL)
    to_visit = [url]
    already_visited = []
    i = 0
    paths = []
    while len(to_visit) > 0:
        print(f'processing {to_visit}')
        docs = load_docs(to_visit)
        current_dest = os.path.join(dest, f'tmp/{i}')
        vector_store(split_docs(html_to_markdown(docs))
                     ).save_local(current_dest)
        paths += [current_dest]
        already_visited += to_visit
        links = extract_links(docs)
        links = [link for link in links if link.startswith(filter)]
        to_visit = [link for link in links if link not in already_visited]
        i += 1
    merge_indexes(dest, paths)
    rmtree(os.path.join(dest, 'tmp'))


def load_docs(urls: List[str]) -> List[Document]:
    loader = AsyncChromiumLoader(urls)
    return loader.load()


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


def embeddings():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def vector_store(docs: List[Document]) -> VectorStore:
    return FAISS.from_documents(docs, embeddings())


def merge_indexes(path: str, src: List[str]):
    vs = FAISS.load_local(src[0], embeddings(),
                          allow_dangerous_deserialization=True)
    for s in src[1:]:
        vs.merge_from(FAISS.load_local(
            s, embeddings(), allow_dangerous_deserialization=True))
    vs.save_local(path)

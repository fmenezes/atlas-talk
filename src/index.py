from typing import Any, List

import ollama
from langchain_text_splitters import MarkdownTextSplitter
from langchain_community.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.vectorstores import VectorStore
from langchain_core.documents import Document

from src import EMBEDDING_MODEL

def load_docs() -> List[Document]:
    loader = DirectoryLoader('./docs', glob='**/*.md',
                             loader_cls=UnstructuredMarkdownLoader)
    return loader.load()


def split_docs(docs: List[Document]) -> List[Document]:
    text_splitter = MarkdownTextSplitter()
    return text_splitter.split_documents(docs)


def vector_store(docs: List[Document]) -> VectorStore:
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    return FAISS.from_documents(docs, embeddings)


def save_index(path: str):
    ollama.pull(EMBEDDING_MODEL)
    vector_store(split_docs(load_docs())).save_local(path)


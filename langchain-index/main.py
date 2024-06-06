from typing import List, Iterable
import os
import uuid
import json

import ollama
from langchain_core.documents import Document
from langchain_community.document_loaders import UnstructuredHTMLLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

EMBEDDING_MODEL = "mxbai-embed-large"


def update_metadata(docs: Iterable[Document]) -> Iterable[Document]:
    for doc in docs:
        doc.metadata['local_path'] = doc.metadata['source']
        metadata_path = doc.metadata['local_path'].removesuffix(
            '.html') + '_metadata.json'
        with open(metadata_path, 'r') as f:
            file_metadata = json.load(f)
            doc.metadata['source'] = file_metadata['url']
        yield doc


def load_docs(paths: tuple[str, ...]) -> Iterable[Document]:
    for path in paths:
        loader = DirectoryLoader(
            path, "*.html", loader_cls=UnstructuredHTMLLoader)
        for doc in loader.load():
            yield doc


def split_docs(docs: Iterable[Document]) -> Iterable[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=10)
    for splitted_doc in text_splitter.split_documents(docs):
        yield splitted_doc


def embeddings() -> Embeddings:
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def setup_docs() -> VectorStore:
    docs = list(split_docs(update_metadata(
        load_docs(('./data/docs/atlas/atlas-cli', './data/docs/atlas/cli')))))
    return FAISS.from_documents(docs, embeddings())


def main() -> None:
    ollama.pull(EMBEDDING_MODEL)
    vs = setup_docs()
    vs.save_local('./data/langchain_index')


if __name__ == "__main__":
    main()

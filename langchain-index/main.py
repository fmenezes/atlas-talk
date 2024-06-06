from typing import Any, List
import os
import uuid
import json

import ollama
from langchain_core.documents import Document
from langchain_community.document_loaders import BSHTMLLoader
from langchain_community.document_transformers import Html2TextTransformer
from langchain_text_splitters import MarkdownTextSplitter
from langchain_core.embeddings import Embeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.vectorstores import VectorStore
from langchain_community.vectorstores import FAISS

EMBEDDING_MODEL = "mxbai-embed-large"


def chunks(lst: List[str], n: int) -> List[List[str]]:
    res = []
    for i in range(0, len(lst), n):
        res += [lst[i:i + n]]
    return res


def split_load() -> List[List[str]]:
    files = []
    for (dirpath, dirnames, filenames) in os.walk('./data/docs'):
        files.extend([os.path.join(dirpath, file)
                     for file in filenames if file.endswith('.html')])
    return chunks(files, 100)


def load_docs(files: List[str]) -> List[Document]:
    print('Loading docs...')
    l = [BSHTMLLoader(f).load() for f in files]
    return [
        entry
        for subl in l
        for entry in subl
    ]


def html_to_markdown(docs: List[Document]) -> List[Document]:
    print('Converting markup to markdown...')
    html2text = Html2TextTransformer()
    return html2text.transform_documents(docs)


def split_docs(docs: List[Document]) -> List[Document]:
    print('Splitting markdown...')
    text_splitter = MarkdownTextSplitter()
    return text_splitter.split_documents(docs)


def embeddings() -> Embeddings:
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def setup_batch(id: str, files: List[str]) -> str:
    dest = f'./data/langchain_index/chunks/{id}'

    if os.path.exists(dest):
        return dest

    docs = split_docs(html_to_markdown(load_docs(files)))
    print('Embedding...')
    vs = FAISS.from_documents(docs, embeddings())
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    vs.save_local(dest)
    return dest


def setup_docs() -> VectorStore:
    map_path = './data/langchain_index/chunks/map.json'
    map = None
    if os.path.exists(map_path):
        with open('./data/langchain_index/chunks/map.json', 'r') as f:
            map = json.load(f)
    else:
        with open('./data/langchain_index/chunks/map.json', 'w') as f:
            batches = split_load()
            map = [{'id': str(uuid.uuid4()), 'files': batch} for batch in batches]
            json.dump(map, f)
    paths = [setup_batch(batch['id'], batch['files']) for batch in map]
    vs = FAISS.load_local(paths[0], embeddings(),
                          allow_dangerous_deserialization=True)
    for path in paths[1:]:
        current_vs = FAISS.load_local(path, embeddings(),
                                      allow_dangerous_deserialization=True)
        vs.merge_from(current_vs)
    return vs


def main() -> None:
    ollama.pull(EMBEDDING_MODEL)
    vs = setup_docs()
    vs.save_local('./data/langchain_index')


if __name__ == "__main__":
    main()

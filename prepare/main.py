from typing import Iterable, Dict, List, Any, Optional
import json
import os
import re

from llama_index.core.node_parser.relational.unstructured_element import UnstructuredElementNodeParser
from llama_index.core import SimpleDirectoryReader, Settings
from llama_index.core.readers.file.base import default_file_metadata_func
from llama_index.core.schema import Document
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.node_parser.file import MarkdownNodeParser, HTMLNodeParser
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
import chromadb
from llama_index.core.schema import TransformComponent

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)
Settings.llm = Ollama(model='llama3')
Settings.embed_model = embed_model

def vector_store(path: str, collection_name: str) -> VectorStore:
    chroma_client = chromadb.PersistentClient(path)
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def load_metadata(p: str) -> Dict:
    default_metadata = default_file_metadata_func(p)

    try:
        if p.endswith('.html'):
            mp = p.removesuffix('.html') + '_metadata.json'
            if os.path.exists(mp):
                with open(mp, "r") as f:
                    metadata = json.load(f)
                    return {
                        'url': metadata['url'],
                        **default_metadata
                    }
    except:
        pass
    
    return default_metadata


class DocsCleaner(TransformComponent):
    def __call__(self, nodes, **kwargs):
        for node in nodes:
            node.text = re.sub(r'^Options(.*)$', 'Flags\1', node.text)
            node.text = re.sub(r'\[(?!flags)([^\[\]]+)\]', '<\1>', node.text)
        return nodes

def walk_srcs(srcs: str | Iterable[str]) -> Iterable[str]:
    if isinstance(srcs, str):
        yield srcs
    else:
        for src in srcs:
            yield src


def load_docs(srcs: str | List[str], required_exts: Optional[List[str]] = None, exclude: Optional[List] = None) -> Iterable[Document]:
    for src in walk_srcs(srcs):
        loader = SimpleDirectoryReader(
            input_dir=src, recursive=True, exclude=exclude, required_exts=required_exts, file_metadata=load_metadata)
        for doc in loader.load_data():
            yield doc


def ingest_html(vector_store: VectorStore, docs: Iterable[Document]):
    pipeline = IngestionPipeline(
        transformations=[
            HTMLNodeParser(),
            SentenceSplitter(chunk_size=200, chunk_overlap=0),
            embed_model,
        ],
        vector_store=vector_store,
    )
    pipeline.run(documents=docs)


def ingest_md(vector_store: VectorStore, docs: Iterable[Document]):
    pipeline = IngestionPipeline(
        transformations=[
            DocsCleaner(),
            MarkdownNodeParser(),
            SentenceSplitter(chunk_size=200, chunk_overlap=0),
            embed_model,
        ],
        vector_store=vector_store,
    )
    pipeline.run(documents=docs)


def main():
    if os.path.exists("./data/index"):
        print('already done')
        exit(0)
    if not os.path.exists("./data/docs"):
        print('data not collected, perhaps run "make collect"')
        exit(1)

    if not os.path.exists("./data/atlascli-command-reference-md"):
        print('docs not captured from atlas cli code')
        exit(1)

    vs = vector_store("./data/index", "atlascli")
    html_docs = load_docs(srcs=('./data/docs/atlas/atlas-cli', './data/docs/atlas/cli', './data/docs/atlas/manage-atlas-cli'),
                          required_exts=['.html'], exclude=['./stable/command'])
    ingest_html(vs, html_docs)

    vs = vector_store("./data/index", "atlascli-commands")
    md_docs = load_docs(srcs='./data/atlascli-command-reference-md', required_exts=['.md'])
    ingest_md(vs, md_docs)


if __name__ == "__main__":
    main()

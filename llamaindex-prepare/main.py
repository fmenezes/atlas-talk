from typing import Iterable, Dict, List, Any, Optional, Sequence
import json
import os
from pathlib import Path

from unstructured.partition.html import partition_html
from llama_index.core.schema import BaseNode
from llama_index.core.node_parser.relational.unstructured_element import UnstructuredElementNodeParser
from llama_index.core.readers.base import BaseReader
from llama_index.core import SimpleDirectoryReader, Settings
from llama_index.core.readers.file.base import default_file_metadata_func
from llama_index.core.schema import Document
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
import chromadb

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)
Settings.llm = Ollama(model='llama3')
Settings.embed_model = embed_model

def vector_store(path: str):
    chroma_client = chromadb.PersistentClient(path)
    chroma_collection = chroma_client.get_or_create_collection("mongodb")
    return ChromaVectorStore(chroma_collection=chroma_collection)


def load_metadata(p: str) -> Dict:
    default_metadata = default_file_metadata_func(p)

    mp = p.removesuffix('.html') + '_metadata.json'
    with open(mp, "r") as f:
        metadata = json.load(f)
        return {
            'url': metadata['url'],
            **default_metadata
        }


def load_docs(srcs: List[str]) -> Iterable[Document]:
    for src in srcs:
        loader = SimpleDirectoryReader(input_dir=src, recursive=True, required_exts=[
            '.html'], file_metadata=load_metadata)
        for doc in loader.load_data():
            yield doc


class CustomNodeParser(UnstructuredElementNodeParser):
    def filter_table(self, table_element: Any) -> bool:
        return False


def ingest(vector_store: VectorStore):
    pipeline = IngestionPipeline(
        transformations=[
            CustomNodeParser(),
            SentenceSplitter(chunk_size=200, chunk_overlap=0),
            embed_model,
        ],
        vector_store=vector_store,
    )
    pipeline.run(documents=load_docs(
        ('./data/docs/atlas/atlas-cli', './data/docs/atlas/cli')))


def main():
    if os.path.exists("./data/llamaindex_index"):
        print('already done')
        exit(0)
    vs = vector_store("./data/llamaindex_index")
    ingest(vs)


if __name__ == "__main__":
    main()

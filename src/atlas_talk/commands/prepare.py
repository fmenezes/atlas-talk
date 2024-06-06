from typing import Iterable, Dict, List, Optional
import os

from llama_index.core import SimpleDirectoryReader, Settings
from llama_index.core.readers.file.base import default_file_metadata_func
from llama_index.core.schema import Document
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.node_parser.file import MarkdownNodeParser
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.vector_stores.types import VectorStore

from . import set_settings, vector_store
from atlas_talk.config import Config

def load_metadata(p: str) -> Dict:
    metadata = default_file_metadata_func(p)

    if "atlascli-command-reference" in p:
        metadata['URL'] = f"https://www.mongodb.com/docs/atlas/cli/stable/command/{os.path.basename(p).replace("_", "-").removesuffix(".md")}/"

    return metadata


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


def ingest(vector_store: VectorStore, docs: Iterable[Document]):
    pipeline = IngestionPipeline(
        transformations=[
            MarkdownNodeParser(),
            SentenceSplitter(chunk_size=200, chunk_overlap=0),
            Settings.embed_model,
        ],
        vector_store=vector_store,
    )
    pipeline.run(documents=docs, show_progress=True)


def execute(args):
    set_settings()

    if os.path.exists(Config.INDEX_PATH):
        print(f'index already found in {Config.INDEX_PATH}')
        exit(0)

    if not os.path.exists("./data/atlascli-command-reference"):
        print('docs not captured from atlas cli code')
        exit(1)

    vs = vector_store()
    md_docs = load_docs(srcs=('./data/atlascli-command-reference', './data/extra'), required_exts=['.md'])
    ingest(vs, md_docs)

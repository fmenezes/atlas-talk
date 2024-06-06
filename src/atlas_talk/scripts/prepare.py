import argparse
import os
from typing import Dict, Iterable, List, Optional

from llama_index.core import Settings, SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.node_parser.file import MarkdownNodeParser
from llama_index.core.readers.file.base import default_file_metadata_func
from llama_index.core.schema import Document
from llama_index.core.vector_stores.types import VectorStore

from atlas_talk.config import Config
from atlas_talk.settings import model, vector_store


def _load_metadata(p: str) -> Dict:
    metadata = default_file_metadata_func(p)

    if "atlascli-command-reference" in p:
        metadata["URL"] = (
            f"https://www.mongodb.com/docs/atlas/cli/stable/command/{os.path.basename(p).replace("_", "-").removesuffix(".md")}/"
        )

    return metadata


def _walk_srcs(srcs: str | Iterable[str]) -> Iterable[str]:
    if isinstance(srcs, str):
        yield srcs
    else:
        yield from srcs


def _load_docs(
    srcs: str | List[str],
    required_exts: Optional[List[str]] = None,
    exclude: Optional[List] = None,
) -> Iterable[Document]:
    for src in _walk_srcs(srcs):
        loader = SimpleDirectoryReader(
            input_dir=src,
            recursive=True,
            exclude=exclude,
            required_exts=required_exts,
            file_metadata=_load_metadata,
        )
        yield from loader.load_data()


def _ingest(vs: VectorStore, docs: Iterable[Document]):
    pipeline = IngestionPipeline(
        transformations=[
            MarkdownNodeParser(),
            SentenceSplitter(chunk_size=200, chunk_overlap=0),
            Settings.embed_model,
        ],
        vector_store=vs,
    )
    pipeline.run(documents=docs, show_progress=True)


def run(env: str) -> None:
    config = Config(env)

    model(config)

    if os.path.exists(config.index_path):
        raise RuntimeError(f"index already found in {config.index_path}")

    vs = vector_store(config)
    md_docs = _load_docs(
        srcs=("./data/atlascli-command-reference", "./data/extra"),
        required_exts=[".md"],
    )
    _ingest(vs, md_docs)


def _main() -> None:
    parser = argparse.ArgumentParser(prog="prepare", description="prepare data for atlas-talk")

    parser.add_argument("--env", type=str, help="env to use", default="default")

    args = parser.parse_args()
    run(env=args.env)


if __name__ == "__main__":
    _main()

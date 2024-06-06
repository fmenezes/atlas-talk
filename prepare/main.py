from typing import Iterable, Dict, List, Optional
import os

from llama_index.core import SimpleDirectoryReader, Settings
from llama_index.core.readers.file.base import default_file_metadata_func
from llama_index.core.schema import Document
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModeModel
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.node_parser.file import MarkdownNodeParser
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.openai import OpenAI
from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL
from llama_index.llms.ollama import Ollama
import chromadb

def set_settings() -> None:
    AI_PLATFORM = os.environ.get('AI_PLATFORM', 'OPENAI')
    if AI_PLATFORM == 'OLLAMA':
        Settings.embed_model = OllamaEmbedding(
            model_name=os.environ.get('OLLAMA_EMBED_MODEL', 'nomic-embed-text')
        )
        Settings.llm = Ollama(model=os.environ.get(
            'OLLAMA_MODEL', 'mistral'), temperature=0.5)
    elif AI_PLATFORM == 'OPENAI':
        Settings.embed_model = OpenAIEmbedding(model=os.environ.get(
            'OPENAI_EMBED_MODEL', OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002))
        Settings.llm = OpenAI(model=os.environ.get(
            'OPENAI_MODEL', DEFAULT_OPENAI_MODEL))


def vector_store(path: str, collection_name: str) -> VectorStore:
    chroma_client = chromadb.PersistentClient(path)
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def load_metadata(p: str) -> Dict:
    metadata = default_file_metadata_func(p)

    metadata['URL'] = f"https://www.mongodb.com/docs/atlas/cli/stable/command/{
        os.path.basename(p).replace("_", "-").removesuffix(".md")}/"

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
    pipeline.run(documents=docs)


def main():
    if os.path.exists("./data/index"):
        print('already done')
        exit(0)
    if not os.path.exists("./data/atlascli-command-reference"):
        print('docs not captured from atlas cli code')
        exit(1)

    set_settings()
    vs = vector_store("./data/index", "atlascli-commands")
    md_docs = load_docs(srcs=('./data/atlascli-command-reference', './data/extra'), required_exts=['.md'])
    ingest(vs, md_docs)


if __name__ == "__main__":
    main()

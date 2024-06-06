from typing import List
import os

from rich.console import Console
from rich.markdown import Markdown
from llama_index.core.query_engine import BaseQueryEngine
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.vector_stores.types import VectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.core.agent.runner.base import AgentRunner

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text"
)

Settings.llm = Ollama(model='llama3')
Settings.embed_model = embed_model

def vector_store(src: str, collection_name: str):
    chroma_client = chromadb.PersistentClient(src)
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
    return ChromaVectorStore(chroma_collection=chroma_collection)


def index(vs: VectorStore) -> VectorStoreIndex:
    return VectorStoreIndex.from_vector_store(vs)


def query_engine_tools() -> List[QueryEngineTool]:
    cli_index = index(vector_store("./data/index", "atlascli"))
    cli_commands_index = index(vector_store(
        "./data/index", "atlascli-commands"))

    return [
        QueryEngineTool(
            query_engine=cli_index.as_query_engine(),
            metadata=ToolMetadata(
                name="cli_agent",
                description="Provides information about MongoDB Atlas CLI / Atlas CLI / atlascli",
            ),
        ),
        QueryEngineTool(
            query_engine=cli_commands_index.as_query_engine(),
            metadata=ToolMetadata(
                name="cli_reference_agent",
                description="Provides command syntax for all commands of MongoDB Atlas CLI / Atlas CLI / atlascli",
            ),
        ),
    ]


def setup() -> AgentRunner:
    if not os.path.exists("./data/index"):
        print('index "./data/index" not found, perhaps run "make prepare"')
        exit(1)
    
    tools = query_engine_tools()
    
    return ReActAgent.from_tools(tools, verbose=True, context="You are atlas-talk assistant, you are an AI assistant capable of answering questions about MongoDB Atlas CLI (also known as atlascli). If you don't know the answer just say you don't know, do not attempt to come up with an answer.")


def invoke(agent: AgentRunner, prompt: str) -> str:
    resp = agent.chat(prompt)

    return f"""{resp.response}
"""


def main():
    console = Console()
    chat_engine = setup()
    while True:
        prompt = input("> ")
        if prompt == "/bye":
            exit()
        output = invoke(chat_engine, prompt)
        console.print(Markdown(output))


if __name__ == "__main__":
    main()

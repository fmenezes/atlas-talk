from typing import Any, List
import uuid

from rich.console import Console
from rich.markdown import Markdown
import ollama
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain_community.document_transformers import Html2TextTransformer
from langchain_text_splitters import MarkdownTextSplitter
from langchain_core.vectorstores import VectorStore
from langchain_community.document_loaders import DirectoryLoader

EMBEDDING_MODEL = "mxbai-embed-large"
CHAT_MODEL = "llama3"

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


def load_docs() -> List[Document]:
    loader = DirectoryLoader('./data/old', glob="**/*.html")
    return loader.load()


def html_to_markdown(docs: List[Document]) -> List[Document]:
    html2text = Html2TextTransformer()
    return html2text.transform_documents(docs)


def split_docs(docs: List[Document]) -> List[Document]:
    text_splitter = MarkdownTextSplitter()
    return text_splitter.split_documents(docs)


def embeddings():
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def vector_store(docs: List[Document]) -> VectorStore:
    return FAISS.from_documents(docs, embeddings())


def prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", """You are an assistant helping the user on how to use MongoDB Atlas CLI. If you don't know the answer make sure to say you don't know do not make up an answer. Answer any use questions based on the context below:
<context>
{context}
</context>"""),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ])


def model() -> BaseChatModel:
    return ChatOllama(model=CHAT_MODEL, temperature=1)


def pull_models():
    ollama.pull(CHAT_MODEL)
    ollama.pull(EMBEDDING_MODEL)


def setup() -> RunnableWithMessageHistory:
    pull_models()

    ret = vector_store(split_docs(html_to_markdown(load_docs()))
                       ).as_retriever()

    rag_chain = RunnableParallel({
        "context": ret,
        "input": RunnablePassthrough()
    }) | prompt() | model() | StrOutputParser()

    rag_chain_with_source = RunnableParallel({
        "context": ret,
        "input": RunnablePassthrough()
    }).assign(answer=rag_chain)

    mem_chain = RunnableWithMessageHistory(
        rag_chain_with_source,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )

    return mem_chain


def convert_output(input: Any) -> str:
    out = input['answer'] + '\n\n### Context'
    for doc in input['context']:
        out += f'\n- {doc.metadata['source']}\n>{doc.page_content}'
    return out


def invoke(chain: RunnableWithMessageHistory, session_id: str, prompt: str) -> str:
    return convert_output(chain.invoke({"input": prompt}, config={"configurable": {"session_id": session_id}}))


def main():
    session_id = str(uuid.uuid1())
    console = Console()
    c = setup()
    while True:
        prompt = input("> ")
        if prompt == "/bye":
            exit()
        output = invoke(c, session_id, prompt)
        console.print(Markdown(output))


if __name__ == "__main__":
    main()

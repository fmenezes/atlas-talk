import ollama
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories.file import FileChatMessageHistory
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.prompts import ChatPromptTemplate

from src import CHAT_MODEL, EMBEDDING_MODEL, INDEX_PATH

store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = FileChatMessageHistory(f"memory/{session_id}.json")
    return store[session_id]


def retriever(path: str) -> VectorStoreRetriever:
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True).as_retriever()


def load_and_retrieve_docs(retriever: VectorStoreRetriever) -> RunnableParallel:
    return RunnableParallel({"context": retriever, "input": RunnablePassthrough()})


def prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", """You are an assistant helping the user on how to use MongoDB Atlas CLI. If you don't know the answer make sure to say you don't know do not make up an answer. Answer any use questions based solely on the context below:
        <context>
        {context}
        </context>"""),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ])


def model() -> BaseChatModel:
    return ChatOllama(model=CHAT_MODEL, temperature=0.3)


def pull_models():
    ollama.pull(CHAT_MODEL)
    ollama.pull(EMBEDDING_MODEL)


def chain() -> RunnableWithMessageHistory:
    pull_models()
    rag_chain = load_and_retrieve_docs(
        retriever(INDEX_PATH)) | prompt() | model() | StrOutputParser()

    return RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )

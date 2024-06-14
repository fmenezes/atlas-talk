"""
Config module for the LLaMA-based AI assistant.

This module provides a set of configurable parameters that can be customized to suit specific use cases.
It loads environment variables from a .env file and allows you to configure various settings, such as system prompt, index path, collection name, ai platform, openai API key, and more.

Classes:
    Config: Provides a flexible configuration framework as part of atlas_talk.

Note:
    This module is designed to be used as part of the atlas-talk application. It provides a way to prepare data for use with that application.
"""

import os
from typing import Optional

import dotenv
from llama_index.embeddings.huggingface.utils import \
    DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
from llama_index.embeddings.openai import OpenAIEmbeddingModeModel
from llama_index.llms.llama_cpp.base import DEFAULT_LLAMA_CPP_GGUF_MODEL
from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL


class Config:
    """
    Provides a flexible configuration framework as part of atlas_talk.
    Allows you to customize various settings, such as system prompt, index path, collection name, ai platform, openai API key, and more.
    """

    def __init__(self, env: Optional[str]):
        """
        Initializes the configuration with optional environment variables.

        Args:
            env (Optional[str]): The environment name, which is used to load the corresponding .env file.

        Raises:
            RuntimeError: If the specified environment is not found or the .env file does not exist.
        """
        self._env: str = env
        self._env_file: Optional[str] = None

        if env is not None and env.strip() != "":
            env_file = f"./env/{env}.env"
            if not os.path.exists(env_file):
                raise RuntimeError(
                    f"configuration {env} not found, file {
                        env_file} must be created"
                )
            self._env_file = env_file

        dotenv.load_dotenv(
            self._env_file, override=True
        )  # loads .env, env/openai.env, env/ollama.env, etc

    @property
    def system_prompt(self) -> str:
        """
        System prompt for the AI assistant.

        Returns:
            str: The system prompt.
        """
        return os.getenv(
            "SYSTEM_PROMPT",
            (
                "You are MongoDB Atlas CLI Help Assistant, you know atlas cli command reference. "
                "You should assume atlas cli is properly installed. When you don't know the answer "
                "try looking up the information first and if you still can't find it say you don't know it, "
                "do not try to make up an answer. Format your answers in Markdown."
            ),
        )

    @property
    def index_path(self) -> str:
        """
        Index path for the AI assistant.

        Returns:
            str: The index path.
        """
        return os.getenv("INDEX_PATH", "./data/index")

    @property
    def collection_name(self) -> str:
        """
        Collection name for the AI assistant.

        Returns:
            str: The collection name.
        """
        return os.getenv("COLLECTION_NAME", "atlascli-commands")

    @property
    def ai_platform(self) -> str:
        """
        AI platform for the AI assistant.

        Returns:
            str: The AI platform.
        """
        return os.getenv("AI_PLATFORM", "OPENAI")

    @property
    def openai_api_key(self) -> Optional[str]:
        """
        OpenAI API key for the AI assistant.

        Returns:
            Optional[str]: The OpenAI API key.
        """
        return os.getenv("OPENAI_API_KEY")

    @property
    def openai_api_base_url(self) -> Optional[str]:
        """
        OpenAI API key for the AI assistant.

        Returns:
            Optional[str]: The OpenAI API key.
        """
        return os.getenv("OPENAI_BASE_URL")

    @property
    def openai_model(self) -> str:
        """
        OpenAI model for the AI assistant.

        Returns:
            str: The OpenAI model.
        """
        return os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)

    @property
    def openai_embed_model(self) -> OpenAIEmbeddingModeModel:
        """
        OpenAI embedding model for the AI assistant.

        Returns:
            OpenAIEmbeddingModeModel: The OpenAI embedding model.
        """
        return OpenAIEmbeddingModeModel[
            os.getenv("OPENAI_EMBED_MODEL", OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002.name)
        ]

    @property
    def ollama_model(self) -> str:
        """
        OLLAMA model for the AI assistant.

        Returns:
            str: The OLLAMA model.
        """
        return os.getenv("OLLAMA_MODEL", "mistral")

    @property
    def ollama_embed_model(self) -> str:
        """
        OLLAMA embedding model for the AI assistant.

        Returns:
            str: The OLLAMA embedding model.
        """
        return os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

    @property
    def llama_cpp_model_url(self) -> str:
        """
        LLama CPP model URL for the AI assistant.

        Returns:
            str: The LLama CPP model URL.
        """
        return os.getenv("LLAMA_CPP_MODEL_URL", DEFAULT_LLAMA_CPP_GGUF_MODEL)

    @property
    def n_gpu_layers(self) -> int:
        """
        Number of GPU layers for the AI assistant.

        Returns:
            int: The number of GPU layers.
        """
        try:
            return int(os.getenv("N_GPU_LAYERS", "-1"))
        except ValueError:
            return -1

    @property
    def llama_cpp_embed_model(self) -> str:
        """
        LLama CPP embedding model for the AI assistant.

        Returns:
            str: The LLama CPP embedding model.
        """
        return os.getenv("LLAMA_CPP_EMBED_MODEL", DEFAULT_HUGGINGFACE_EMBEDDING_MODEL)

    @property
    def skip_rag(self) -> bool:
        """
        Flag to skip RAG for the AI assistant.

        Returns:
            bool: The flag.
        """
        try:
            return os.getenv("SKIP_RAG", "False").lower() in ("true", "1", "t")
        except ValueError:
            return False

    @property
    def skip_docs(self) -> bool:
        """
        Flag to skip fetch_docs tool for the AI assistant.

        Returns:
            bool: The flag.
        """
        try:
            return os.getenv("SKIP_DOCS", "False").lower() in ("true", "1", "t")
        except ValueError:
            return False

    @property
    def skip_atlascli_tools(self) -> bool:
        """
        Flag to skip atlascli tool for the AI assistant.

        Returns:
            bool: The flag.
        """
        try:
            return os.getenv("SKIP_ATLASCLI_TOOLS", "False").lower() in ("true", "1", "t")
        except ValueError:
            return False

    @property
    def cookie(self) -> Optional[str]:
        """
        The http cookie to be used by the http client to make the api calls to the model.

        Returns:
            str: The http cookie to be used.
        """
        return os.getenv("COOKIE")

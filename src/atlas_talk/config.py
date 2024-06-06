import os
from typing import Optional

import dotenv
from llama_index.embeddings.huggingface.utils import \
    DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
from llama_index.embeddings.openai import OpenAIEmbeddingModeModel
from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL
from llama_index.llms.llama_cpp import DEFAULT_LLAMA_CPP_GGUF_MODEL


class Config:
    def __init__(self, env: Optional[str]):
        self.env: str = env
        self.env_file: Optional[str] = None

        if env is not None and env.strip() != "":
            env_file = f"./env/{env}.env"
            if not os.path.exists(env_file):
                raise RuntimeError(
                    f"configuration {env} not found, file {env_file} must be created"
                )
            self.env_file = env_file

        dotenv.load_dotenv(
            self.env_file, override=True
        )  # loads .env, env/openai.env, env/ollama.env, etc

        self.system_prompt: Optional[str] = os.getenv("SYSTEM_PROMPT")
        self.index_path: str = os.getenv("INDEX_PATH", "./data/index")
        self.collection_name: str = os.getenv("COLLECTION_NAME", "atlascli-commands")
        self.ai_platform: str = os.getenv("AI_PLATFORM", "OPENAI")
        self.openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
        self.openai_model: str = os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
        self.openai_embed_model: str = os.getenv(
            "OPENAI_EMBED_MODEL", OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002
        )
        self.ollama_model: str = os.getenv("OLLAMA_MODEL", "mistral")
        self.ollama_embed_model: str = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
        self.llama_cpp_model_url: str = os.getenv(
            "LLAMA_CPP_MODEL_URL",
            DEFAULT_LLAMA_CPP_GGUF_MODEL
        )
        try:
            n_gpu_layers = int(
                os.getenv(
                    "N_GPU_LAYERS",
                    "-1",
                )
            )
        except ValueError:
            n_gpu_layers = -1
        self.n_gpu_layers: int = n_gpu_layers
        self.llama_cpp_embed_model: str = os.getenv(
            "LLAMA_CPP_EMBED_MODEL", DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
        )
        self.skip_rag: bool = os.getenv("SKIP_RAG", "False").lower() in (
            "true",
            "1",
            "t",
        )

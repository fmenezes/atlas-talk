import os
from typing import Optional

import dotenv
from llama_index.embeddings.huggingface.utils import \
    DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
from llama_index.embeddings.openai import OpenAIEmbeddingModeModel
from llama_index.llms.openai.base import DEFAULT_OPENAI_MODEL


class Config:
    def __init__(self, env: str = "default"):
        self.env: str = env
        self.env_file: str = f"./env/{env}.env"

        if not os.path.exists(self.env_file):
            raise RuntimeError(
                f"configuration {env} not found, file {self.env_file} must be created"
            )

        values = dotenv.dotenv_values(self.env_file)  # loads openai.env, ollama.env, etc

        self.system_prompt: Optional[str] = values.get("SYSTEM_PROMPT")
        self.index_path: str = values.get("INDEX_PATH", "./data/index")
        self.collection_name: str = values.get("COLLECTION_NAME", "atlascli-commands")
        self.ai_platform: str = values.get("AI_PLATFORM", "OPENAI")
        self.openai_api_key: Optional[str] = values.get("OPENAI_API_KEY")
        self.openai_model: str = values.get("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
        self.openai_embed_model: str = values.get(
            "OPENAI_EMBED_MODEL", OpenAIEmbeddingModeModel.TEXT_EMBED_ADA_002
        )
        self.ollama_model: str = values.get("OLLAMA_MODEL", "mistral")
        self.ollama_embed_model: str = values.get("OLLAMA_EMBED_MODEL", "nomic-embed-text")
        self.llama_cpp_model_url: str = values.get(
            "LLAMA_CPP_MODEL_URL",
            "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q4_0.gguf",
        )
        try:
            n_gpu_layers = int(
                values.get(
                    "N_GPU_LAYERS",
                    "-1",
                )
            )
        except ValueError:
            n_gpu_layers = -1
        self.n_gpu_layers: int = n_gpu_layers
        self.llama_cpp_embed_model: str = values.get(
            "LLAMA_CPP_EMBED_MODEL", DEFAULT_HUGGINGFACE_EMBEDDING_MODEL
        )
        self.skip_rag: bool = values.get("SKIP_RAG", "False").lower() in (
            "true",
            "1",
            "t",
        )

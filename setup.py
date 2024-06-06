import os
import platform
from setuptools import setup, find_packages

if platform.system() == "Darwin" and platform.machine() == "arm64":
    os.environ['CMAKE_ARGS'] = "-DLLAMA_METAL=on"

setup(
    name="atlas_talk",
    version="0.0.1",
    author="Filipe C Menezes <fcmenezes87@gmail.com>",
    author_email="fcmenezes87@gmail.com",
    description="MongoDB Atlas CLI interactive help cli",
    url="https://github.com/fmenezes/atlas-talk",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.11",
    extras_require={
        "dev": [
            "pytest",
        ],
    },
    install_requires=[
        "rich",
        "chromadb",
        "llama-index",
        "llama-index-vector-stores-chroma",
        "llama-index-readers-web",
        "llama-index-llms-ollama",
        "llama-index-embeddings-ollama",
        "llama-index-llms-llama-cpp",
        "llama-index-embeddings-huggingface",
        "yaspin"
    ]
)

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

# Use mxbai-embed-large for embeddings
embed_model = OllamaEmbedding(model_name="mxbai-embed-large")

# Use DeepSeek for inference via Ollama
llm = Ollama(model="deepseek-r1:1.5b")

# Load documents from a directory (where PDFs are stored)
documents = SimpleDirectoryReader(input_dir="./data").load_data()

# Create an index with mxbai embeddings
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

# Save the index
index.storage_context.persist(persist_dir="./index")

print("Index created using mxbai embeddings and saved successfully.")

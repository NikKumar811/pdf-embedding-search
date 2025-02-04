from llama_index.core import load_index_from_storage, StorageContext, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Explicitly set OllamaEmbedding as the default
Settings.embed_model = OllamaEmbedding(model_name="mxbai-embed-large")

# Define storage context for loading the index
storage_context = StorageContext.from_defaults(persist_dir="./index")

# Load the saved index with the storage context
index = load_index_from_storage(storage_context=storage_context)

# Use DeepSeek-R1 via Ollama for inference
llm = Ollama(model="deepseek-r1:1.5b")

# Create a query engine
query_engine = index.as_query_engine(llm=llm)

# Query the document
query = "What is this document about?"
response = query_engine.query(query)

print("Answer:", response)

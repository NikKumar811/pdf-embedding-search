import requests
import json

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama2", "prompt": "Write a poem about AI"},
    stream=True
)

poem = ""
for line in response.iter_lines():
    if line:
        data = json.loads(line)
        poem += data.get("response", "") 

print(poem) 

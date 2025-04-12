# Project Title

RAG with mistral 

## Description
This repository demonstrates a lightweight and efficient Retrieval-Augmented Generation (RAG) pipeline using:

🧠 Mistral LLM via Ollama

📚 Document loading & chunking with LangChain

📦 Vector similarity search using FAISS

📝 Supports .docx files as knowledge source (can be extended to PDFs, text, etc.)

🧰 Tech Stack
LangChain – for document loading and text splitting

Sentence-Transformers – for generating embeddings

FAISS – for fast vector similarity search

Ollama – to run Mistral or other local LLMs

Python-Docx – to load .docx documents

### Installing

Installation
1. Clone the repository
 ```
git clone https://github.com/codersbranch/labs
cd labs/ragwithmistral
```

2. Create a virtual environment (optional but recommended)
```
python -m venv venv
```
Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```
On macOS/Linux:
```
source venv/bin/activate
```

3. Install required Python packages
 ```
pip install langchain sentence-transformers faiss-cpu ollama python-docx numpy langchain-community docx2txt
```


4. Install Ollama
If you haven't already installed Ollama, follow the instructions at Ollama's official website.

Make sure you have at least one model downloaded using:
```
ollama pull mistral
```
or any other model of your choice.

### Executing program
* How to run the program
```
python rag_doc_mistral.py
```

## Authors
 CodersBranch codebase24@gmail.com


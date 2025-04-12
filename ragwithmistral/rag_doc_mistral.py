# 1. Install required packages (added python-docx for docx handling)
# pip install langchain sentence-transformers faiss-cpu ollama python-docx

import ollama
from langchain_community.document_loaders import Docx2txtLoader  # Changed to DOCX loader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 2. Load and process Word document
def load_docx_documents(file_path):  
    loader = Docx2txtLoader(file_path)
    return loader.load()


def split_documents(pages):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return text_splitter.split_documents(pages)


def create_vector_store(split_docs):
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    document_texts = [doc.page_content for doc in split_docs]
    embeddings = embedder.encode(document_texts)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings.astype(np.float32))
    return index, document_texts, embedder

# 5. Retrieve relevant context
def retrieve_context(query, embedder, index, documents, k=3):
    query_embedding = embedder.encode([query])
    distances, indices = index.search(query_embedding.astype(np.float32), k)
    return [documents[i] for i in indices[0]]

# 6. Generate answer using Ollama 
def generate_answer_with_ollama(query, context):
    formatted_context = "\n".join(context)
    
    prompt = f"""You are an expert assistant trained on document information.
    Use this context to answer the question:
    
    {formatted_context}
    
    Question: {query}
    
    Answer in detail using only the provided context:"""
    #  model='gemma:2b',
    response = ollama.generate(
      
        model='tinyllama:latest', 
        prompt=prompt,
        options={
            'temperature': 0.3,
            'max_tokens': 2000
        }
    )
    return response['response']

# Main workflow 
def main(file_path, query):
    # Load and process DOCX file
    pages = load_docx_documents(file_path)
    split_docs = split_documents(pages)
    
    # Create vector store
    index, document_texts, embedder = create_vector_store(split_docs)
    
    # Retrieve context
    context = retrieve_context(query, embedder, index, document_texts)
    
    # Generate answer
    answer = generate_answer_with_ollama(query, context)
    return answer

# Example usage
if __name__ == "__main__":
    file_path = "Product_Manual_Sample.docx" 
    query = "when should I replace HEPA filter?"
    
    result = main(file_path, query)
    print("Answer:", result)
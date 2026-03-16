from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import requests

# Initialize embedding model
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

chroma_client = PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(name="medical_docs")

def index_document(doc_id, text):
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = embed_model.encode(chunks).tolist()
    ids = [f"{doc_id}_{i}" for i in range(len(chunks))]
    collection.add(documents=chunks, embeddings=embeddings, ids=ids)

def query_ollama(prompt):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",  
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

def get_chat_response(query, full_context_text):
    index_document("latest_doc", full_context_text)

    query_embedding = embed_model.encode([query])[0].tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=3)

    relevant_chunks = " ".join(results["documents"][0])
    prompt = (
        f"You are a helpful medical assistant.\n"
        f"Based on the following report and context, answer the user's question.\n\n"
        f"Context:\n{relevant_chunks}\n\n"
        f"Question: {query}\n\n"
        f"Answer:"
    )

    return query_ollama(prompt).strip()
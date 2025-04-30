from langchain.embeddings import HuggingFaceEmbeddings
from app.extensions import mongo
from flask import current_app

# Using small, fast, and accurate model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def insert_document(text: str):
    client = mongo.db
    collection_name = current_app.config["MONGO_COLLECTION"]
    collection = client[collection_name]
    vector = embedding_model.embed_query(text)
    
    
    
    print(f"Using collection: {collection_name}")
    if not collection_name:
        raise ValueError("MONGO_COLLECTION not configured properly.")
    
    # Insert the document into the specified collection
    collection.insert_one({
        "text": text,
        "vector": vector
    })

    print(f"Document inserted: {text[:50]}...")  # Print first 50 characters of the inserted text


def query_similar_documents(query, k=3):
    vector = embedding_model.embed_query(query)
    
    results = mongo.db[current_app.config["MONGO_COLLECTION"]].aggregate([
        {
            "$vectorSearch": {
                "queryVector": vector,
                "path": "vector",
                "numCandidates": 100,
                "limit": k,
                "index": "vector_index"
            }
        }
    ])
    
    return [doc["text"] for doc in results]

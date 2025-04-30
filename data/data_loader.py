import sys
sys.path.append("..")

from app import create_app
from app.services.vector_store import insert_document

app = create_app()
app.app_context().push()

documents = [
    "Flask is a Python web framework for building APIs and web apps.",
    "MongoDB is a document-oriented NoSQL database.",
    "Vector databases allow semantic similarity search using embeddings."
]

for doc in documents:
    result = insert_document(doc)
    print(f"Document '{doc}' inserted: {result}")
    if result is None:
        print("Warning: insert_document returned None")

print("Documents inserted.")

# from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo

# app = Flask(__name__)

# # Initialize MongoDB client
# mongo = PyMongo(app)

# @app.route('/insertDocument', methods=['POST'])
# def insert_document():
#     doc = request.get_json()['doc']
#     collection_name = "pdf"
#     result = mongo.db[collection_name].insert_one({'text': doc})
#     return jsonify({'message': f"Document '{doc}' inserted: {result.inserted_id}"})

# if __name__ == '__main__':
#     app.run(debug=True)
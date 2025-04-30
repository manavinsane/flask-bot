from flask import Blueprint, request, jsonify
from app.services.rag_pipeline import generate_answer

rag_bp = Blueprint('rag', __name__)

@rag_bp.route('/rag', methods=['POST'])
def rag_query():
    data=request.json
    question = data.get('question')
    if not question:
        return jsonify({'error': 'No question provided'}), 400
    answer = generate_answer(question)
    return jsonify({'answer': answer})
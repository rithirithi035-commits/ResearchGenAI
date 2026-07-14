from flask import Blueprint, request, jsonify
from services.ollama_service import ask_ollama

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    prompt = data.get("prompt", "")

    answer = ask_ollama(prompt)

    return jsonify({
        "response": answer
    })
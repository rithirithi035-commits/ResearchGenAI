from flask import Blueprint, request, jsonify
from agents.research_agent import research_topic

research_bp = Blueprint("research", __name__)

@research_bp.route("/research", methods=["POST"])
def research():

    data = request.get_json()

    topic = data.get("topic", "")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    result = research_topic(topic)

    return jsonify({
        "topic": topic,
        "research": result
    })
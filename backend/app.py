from flask import Flask
from flask_cors import CORS

from routes.chat_routes import chat_bp
from routes.research_routes import research_bp   # <-- Add this

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)
app.register_blueprint(research_bp)   # <-- Add this

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "ResearchGen AI Backend is Running 🚀"
    }

if __name__ == "__main__":
    app.run(debug=True)
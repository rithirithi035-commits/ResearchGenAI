from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)

@app.route("/")
def home():
    return {
        "status": "success",
        "message": "ResearchGen AI Backend is Running 🚀"
    }

if __name__ == "__main__":
    app.run(debug=True)
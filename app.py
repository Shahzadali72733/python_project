from flask import Flask
import os
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Home route accessed")
    return "Flask app running on Railway 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    logging.info(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port)

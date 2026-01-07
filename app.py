import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app running 🚀"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/process")
def process():
    import pandas as pd
    import numpy as np
    import nltk
    # your processing logic here
    return "Processing done!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

import os
import sys
import logging
from flask import Flask

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    logger.info("Home route accessed")
    return "Flask app running successfully!"

@app.route("/health")
def health():
    return "OK", 200

@app.route("/process")
def process():
    try:
        import pandas as pd
        import numpy as np
        import nltk
        # your processing logic here
        return "Processing done!"
    except Exception as e:
        logger.error(f"Error in process route: {e}")
        return f"Error: {str(e)}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port)

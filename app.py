from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask app running 🚀"

@app.route("/process")
def process():
    import pandas as pd
    import numpy as np
    import nltk
    # your processing logic here
    return "Processing done!"

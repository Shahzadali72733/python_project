import logging
import os
import sys

from flask import Flask, render_template, request

from beauty_model_01 import predict_beauty_score
from mewati_model import MORPH_FEATURES, normalize_sentence

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    beauty_input = ""
    beauty_result = None
    mewati_input = ""
    mewati_rows = None
    mewati_error = None

    if request.method == "POST":
        form_id = request.form.get("form_id")

        if form_id == "beauty":
            beauty_input = request.form.get("text", "").strip()
            if beauty_input:
                beauty_result = predict_beauty_score(beauty_input)
                logger.info("Beauty model prediction generated")
            else:
                logger.info("Beauty form submitted without input")

        elif form_id == "mewati":
            mewati_input = request.form.get("mewati_text", "").strip()
            normalized = normalize_sentence(mewati_input)
            if normalized:
                mewati_rows = MORPH_FEATURES.get(normalized)
                if not mewati_rows:
                    mewati_error = f"No morphological features found for: {normalized}"
            else:
                mewati_error = "Please enter a sentence."

    sample_sentences = list(MORPH_FEATURES.keys())[:10]  # show a few examples

    return render_template(
        "index.html",
        beauty_result=beauty_result,
        beauty_input=beauty_input,
        mewati_input=mewati_input,
        mewati_rows=mewati_rows,
        mewati_error=mewati_error,
        sample_sentences=sample_sentences,
    )


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)

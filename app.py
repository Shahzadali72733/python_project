import logging
import os
import sys

from flask import Flask, render_template, request

from beauty_model_01 import predict_beauty_score

# Configure logging for PythonAnywhere/Gunicorn
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """Render form and return model output."""
    user_input = ""
    result = None

    if request.method == "POST":
        user_input = request.form.get("text", "").strip()
        if user_input:
            result = predict_beauty_score(user_input)
            logger.info("Prediction generated for input")
        else:
            logger.info("No input provided")

    return render_template("index.html", result=result, user_input=user_input)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    logger.info(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)

from flask import Flask
import firstprogramm  # replace with your script names if needed
import mewati_model
import R_Analysis

app = Flask(__name__)

@app.route("/")
def home():
    return "Python project is LIVE 🚀"

# Optional: you can call your existing functions here
@app.route("/run-first")
def run_first():
    firstprogramm.main()  # if your script has a main() function
    return "firstprogramm ran successfully"

if __name__ == "__main__":
    app.run()

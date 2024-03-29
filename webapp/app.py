from flask import Flask, request, render_template, jsonify
import pandas as pd
import pickle

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    """Return the main page."""
    return render_template("index.html")


# Load pickle with logistic regression model
with open("webapp/model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/output", methods=["GET", "POST"])
def output():
    """Retun text from user input"""
    data = request.get_json(force=True)
    # store user input data in pandas dataframe
    df = pd.DataFrame(data=[data])
    # store predictions from model
    predictions = model.predict_proba(df).round(2)
    output = {
        "probability to continue using the app": predictions[0][0],
        "probability to stop using the app": predictions[0][1],
    }
    # output dictionary to web
    return jsonify(output)

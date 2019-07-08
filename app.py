from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    """Return the main page."""
    return render_template("index.html")

# with open('pkl/model.pkl', 'rb') as f:
#     model = pickle.load(f)

# def prediction(user_input, model):
#     """Predict when a user will drop off the application"""
#     user_input = np.array((user_input))
#     df = pd.DataFrame(user_input).T
#     probability = model.predict_proba(df)
#     return probability

@app.route("/output", methods=["GET", "POST"])
def output():
    """Retun text from user input"""
    data = request.get_json(force=True)
    # print the user input data to console
    print(data)
    # store user input data in dictionary
    df = pd.DataFrame(data=[data])
    print(df)
    # output dictionary to web
    return jsonify(data)
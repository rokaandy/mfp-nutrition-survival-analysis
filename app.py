from flask import Flask, request, render_template, jsonify
import pickle

# # Load model
with open('pkl/model.pkl', 'rb') as f:
    model = pickle.load(f)

features_names = ['days','achievement','calories_10_pct','carbs_10_pct','fat_10_pct',
            'fiber_10_pct','protein_10_pct','sodium_10_pct','sugar_10_pct']

app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    """Return the main page."""
    return render_template("index.html")


@app.route("/output", methods=["GET", "POST"])
def output():
    """Retun text from user input"""
    data = request.get_json(force=True)
    # every time the user_input identifier
    print(data)
    return jsonify(data["user_input"])
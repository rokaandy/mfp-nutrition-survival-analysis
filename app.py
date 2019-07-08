from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    """Return the main page."""
    return render_template("index.html")

@app.route("/output", methods=["GET", "POST"])
def output():
    """Retun text from user input"""
    data = request.get_json(force=True)
    # print the user input data to console
    print(data)
    # store user input data in dictionary
    output = {"calories": data["calories"],
              "carbs": data["carbs"]}
    # output dictionary to web
    return jsonify(output)
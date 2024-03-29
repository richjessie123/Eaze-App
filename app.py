from flask import Flask, render_template, request

# Instantiating the app
app = Flask(__name__)


# Handle HTTP Requests
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        type = request.form["type"]

    return render_template("index.html")


# Running the app
app.run(debug=True, port=5001)

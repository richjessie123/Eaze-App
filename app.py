from flask import Flask, render_template

# Instantiating the app
app = Flask(__name__)

# Handle HTTP Requests
@app.route("/")
def index():
    return render_template ("index.html")

# Running the app
app.run(debug=True, port=5001)

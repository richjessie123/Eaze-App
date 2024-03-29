from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# Instantiating the app
app = Flask(__name__)

# Setting parameters
app.config["SECRET_KEY"] = "youcannothackthis"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Instantiating SQL
db = SQLAlchemy(app)


# Create Database class
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    type = db.Column(db.String(80))


# Handle HTTP Requests
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Extracting variables of sign up form from html file
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["password"]
        type = request.form["re-enter_password"]

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # Running the app
    app.run(debug=True, port=5001)

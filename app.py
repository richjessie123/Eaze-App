from flask import Flask, render_template, request, flash
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
    # confirm_password = db.Column(db.String(80))
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
        confirm_password = request.form["re-enter_password"]
        type = request.form["type"]

        signup_form = Form(first_name=first_name, last_name=last_name,
                           email=email, username=username, password=password,
                           type=type)

        if password == confirm_password:
            db.session.add(signup_form)
            db.session.commit()
        else:
            flash("Passwords do not match", "error")

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # Running the app
    app.run(debug=True, port=5001)

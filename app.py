from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

# Instantiating the app
app = Flask(__name__)

# Setting parameters
app.config["SECRET_KEY"] = "youcannothackthis"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['MAIL_SERVER'] = 'smtp-relay.brevo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "richardjadupoku@gmail.com"
app.config['MAIL_PASSWORD'] = 'cTf3OHtSq5QxZ4nE'

# Instantiating SQL
db = SQLAlchemy(app)

# Mail Instance
mail = Mail(app)


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


# Handle HTTP Requests for main page
@app.route("/", methods=["GET", "POST"])
def index():
    # Get email and username entries
    email_entries = [email.email for email in Form.query.all()]
    username_entries = [username.username for username in Form.query.all()]

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

        # Display error messages if username and email already exist
        if username in username_entries:
            flash("There is an account with this username,"
                  " try a new username or sign in if you already have an account", "info")
        if email in email_entries:
            flash("There is an account with this email,"
                  " try a new email or sign in if you already have an account", "info")

        # Email body and structure
        message_body = (f"{first_name}, \n \n"
                        f"Welcome to the Eaze family. We are pleased that you chose to join us. \n \n"
                        f"{username} is your username \n \n"
                        f"Thank you!"
                        )

        message = Message(subject="Welcome to Eaze!",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)

        # Only add data to database and send email, if password and confirm password match and there
        # is no duplicate email or username
        if password == confirm_password and username not in username_entries and email not in email_entries:
            db.session.add(signup_form)
            db.session.commit()
            mail.send(message)

    return render_template("index.html")


# Handle HTTP requests for sign in page
@app.route("/signin", methods=["GET", "POST"])
def sign_in():
    # Get email and username entries
    email_entries = [email.email for email in Form.query.all()]
    password_entries = [password.password for password in Form.query.all()]

    if request.method == "POST":
        # Extracting variables of sign up form from html file
        email = request.form["email"]
        password = request.form["password"]

        # Display error messages if email and password is incorrect
        if email not in email_entries and password in password_entries:
            flash("There is no account with this email/password,"
                  " try again or register if you don't have an account with us", "info")
        if email in email_entries and password not in password_entries:
            flash("There is no account with this email/password,"
                  " try again or register if you don't have an account with us", "info")
        if email not in email_entries and password not in password_entries:
            flash("You don't seem to have an account with us,"
                  " try again or register if you don't have an account with us", "info")

    return render_template("sign_in.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # Running the app
    app.run(debug=True, port=5001)

from flask import render_template, request, flash, Blueprint
from login.sign_up import Form

# Instantiating the Blueprint
sign_in_blueprint = Blueprint('sign_in_blueprint', __name__)


# Handle HTTP requests for sign in page
@sign_in_blueprint.route("/signin", methods=["GET", "POST"])
def sign_in():
    # Get email and username entries
    email_entries = [email.email for email in Form.query.all()]
    password_entries = [password.password for password in Form.query.all()]

    if request.method == "POST":
        # Extracting variables of login form from html file
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

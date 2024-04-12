
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

# Create the Flask app instance
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

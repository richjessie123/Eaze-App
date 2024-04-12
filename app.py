from extensions import app, db, mail
from login.sign_up import sign_up_blueprint
from login.sign_in import sign_in_blueprint

# Register Blueprints
app.register_blueprint(sign_up_blueprint)
app.register_blueprint(sign_in_blueprint)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # Running the app
    app.run(debug=True, port=5001)

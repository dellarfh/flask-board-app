from flask import Flask
from board import pages, database   # import database.py

def create_app():
    app = Flask(__name__)

    # config database
    app.config.from_mapping(
        DATABASE="database.db",
    )

    # register blueprint
    app.register_blueprint(pages.bp)

    # register db commands
    database.init_app(app)

    return app


from flask import Flask
from .db import init_db


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    # app.config["MONGO_URI"] = "mongodb://admin:admin@mongodb/usuarios?authSource=admin"

    init_db(app)

    return app

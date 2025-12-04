from flask import Flask
from .db import init_db


def create_app(config_filename):
    app = Flask(__name__)
    # ideal seria pegar a config do arquivo
    # porem o formato e diferente do utilizado no mongoengine
    # (que e utilizado no curso)
    # app.config.from_pyfile(config_filename)
    app.config["MONGO_URI"] = "mongodb://admin:admin@mongodb/usuarios?authSource=admin"

    init_db(app)

    return app

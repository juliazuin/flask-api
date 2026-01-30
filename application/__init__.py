from flask import Flask
from .db import init_db
from .app import healthcheck, home, create_user, get_users


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    init_db(app)

    # Registrar as rotas
    app.add_url_rule("/", "home", home)
    app.add_url_rule("/users", "create_user", create_user, methods=["POST"])
    app.add_url_rule("/users", "get_users", get_users, methods=["GET"])
    app.add_url_rule("/health", "healthcheck", healthcheck, methods=["GET"])

    return app

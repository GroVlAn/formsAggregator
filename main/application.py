from flask import Flask
from main.config import config_by_name, Config


def create_app(conf: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(conf)

    return app

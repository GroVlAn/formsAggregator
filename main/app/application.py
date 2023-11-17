from flask import Flask
from flask_cors import CORS

from main.config.config import Config
from main.controllers import bluePrints


def create_app(conf: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(conf)

    app.app_context().push()

    CORS(app)
    for blueprint in bluePrints:
        app.register_blueprint(blueprint)

    return app

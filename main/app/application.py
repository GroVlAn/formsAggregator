import logging
import sys
from typing import Self

from flask import Flask
from flask_cors import CORS
from main.config.config import Config, config_by_name


class FormsApplication:

    _instance: Self = None
    _conf: Config = None
    _app: Flask = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FormsApplication, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    @classmethod
    def set_config(cls, mode: str = ''):
        if mode == '':
            args = sys.argv
            mode = 'dev'

            if '--prod' in args:
                mode = 'prod'

            if '--dev' in args:
                mode = 'dev'

        cls._conf = config_by_name[mode]

    @classmethod
    def get_config(cls) -> Config:
        return cls._conf

    @classmethod
    def create_app(cls):
        cls._app = Flask(__name__)
        cls._app.config.from_object(cls._conf)
        cls._app.logger.info(cls._conf)
        cls._app.app_context().push()

        CORS(cls._app)

    @classmethod
    def get_app(cls) -> Flask:
        return cls._app

    @classmethod
    def run(cls):
        from waitress import serve
        logger = logging.getLogger('waitress')
        logger.setLevel(logging.DEBUG)
        serve(cls._app, host=cls._conf.HOST, port=cls._conf.PORT)

# def create_app(conf: Config) -> Flask:
#     app = Flask(__name__)
#     app.config.from_object(conf)
#     app.logger.info(conf)
#     app.app_context().push()
#
#     CORS(app)
#     for blueprint in bluePrints:
#         app.register_blueprint(blueprint)
#
#     return app

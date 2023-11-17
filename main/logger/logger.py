import json
from datetime import datetime
from typing import List

from flask import Flask


def _arg_to_string(arg: any) -> str:
    """
    func for transform argument from logger to string
    :param arg: any
    :return: string
    """

    if type(arg) == 'dict':
        return json.dumps(arg)

    if type(arg) == 'list':
        return ''.join(arg)

    return arg


class Logger:
    """
    Class wrapper for flask logs
    self.app: Flask - Flask application
    """

    _instance = None
    _app: Flask

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    @classmethod
    def set_app(cls, app: Flask):
        cls._app = app

    @staticmethod
    def _make_text(*args: List[any]) -> str:
        """
        Method for create string for logging from args
        :param args: List[any]
        :return: string
        """

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'{current_time}: ' + ''.join([f'{_arg_to_string(arg)}\t' for arg in args])

    @classmethod
    def info(cls, *args: List[any]):
        """
        print log type INFO
        :param args: List[any]
        :return: None
        """

        cls._app.logger.info(cls._make_text(*args))

    @classmethod
    def debug(cls, *args: List[any]):
        """
        print log type DEBUG
        :param args: List[any]
        :return: None
        """

        cls._app.logger.debug(cls._make_text(*args))

    @classmethod
    def warning(cls, *args: List[any]):
        """
        print log type WARNING
        :param args: List[any]
        :return: None
        """

        cls._app.logger.warning(cls._make_text(*args))

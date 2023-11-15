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

    def __init__(self, app: Flask):
        self.app = app

    @staticmethod
    def _make_text(*args: List[any]) -> str:
        """
        Method for create string for logging from args
        :param args: List[any]
        :return: string
        """

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'{current_time}: ' + ''.join([f'{_arg_to_string(arg)}\t' for arg in args])

    def info(self, *args: List[any]):
        """
        print log type INFO
        :param args: List[any]
        :return: None
        """

        self.app.logger.info(self._make_text(*args))

    def debug(self, *args: List[any]):
        """
        print log type DEBUG
        :param args: List[any]
        :return: None
        """

        self.app.logger.debug(self._make_text(*args))

    def warning(self, *args: List[any]):
        """
        print log type WARNING
        :param args: List[any]
        :return: None
        """

        self.app.logger.warning(self._make_text(*args))

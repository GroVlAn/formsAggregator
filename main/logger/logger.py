import json
from datetime import datetime

from flask import Flask


def _arg_to_string(arg: any):
    if type(arg) == 'dict':
        return json.dumps(arg)

    if type(arg) == 'list':
        return ''.join(arg)

    return arg


class Logger:

    def __init__(self, app: Flask):
        self.app = app

    @staticmethod
    def _make_text(*args):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return f'{current_time}: ' + ''.join([f'{_arg_to_string(arg)}\t' for arg in args])

    def info(self, *args):
        self.app.logger.info(self._make_text(*args))

    def debug(self, *args):
        self.app.logger.debug(self._make_text(*args))

    def warning(self, *args):
        self.app.logger.warning(self._make_text(*args))

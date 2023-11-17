from flask import Blueprint

from main.logger import appLogger

main_print = Blueprint('main_api', __name__)


@main_print.route('/')
def main():
    appLogger.info('/', 'get', 'main')

    return 'hello'

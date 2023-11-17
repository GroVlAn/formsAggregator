import logging

from main import conf, app


def run():
    from waitress import serve
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.DEBUG)
    serve(app, host=conf.HOST, port=conf.PORT)


if __name__ == '__main__':
    run()

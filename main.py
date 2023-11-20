from main import application
from main.controllers import bluePrints



def run():

    for bluePrint in bluePrints:
        application.get_app().register_blueprint(bluePrint)

    application.run()


if __name__ == '__main__':
    run()

import pytest

from main import application, db
from main.controllers import bluePrints
from main.repository.forms_repository import FormsMongoRepository
from main.services.forms_service import FormsService


for bluePrint in bluePrints:
    application.get_app().register_blueprint(bluePrint)


@pytest.fixture()
def app():

    yield application.get_app()


@pytest.fixture(scope='session')
def forms_repository():

    forms_repository = FormsMongoRepository(db['test_form'])

    yield forms_repository

    db['test_form'].drop()


@pytest.fixture()
def forms_service(forms_repository):

    forms_service = FormsService(repos=forms_repository)

    yield forms_service


@pytest.fixture()
def client(app):

    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

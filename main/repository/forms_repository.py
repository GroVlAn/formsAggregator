from typing import Dict, List

from pymongo.database import Database

from main.config.config import FORM_DOCUMENT
from main.logger import appLogger
from main.models.form import Form
from main.repository.interfaces.i_forms_repository import ReposForms


class FormsMongoRepository(ReposForms):
    """
    Class for work with database (work with forms).
    """

    _instance = None
    _db = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(FormsMongoRepository, cls).__new__(cls, *args, **kwargs)

        return cls._instance

    @classmethod
    def set_db(cls, db: Database):
        cls._db = db

    @classmethod
    def create_form(cls, form: Form) -> int:
        """
        method for create new form in mongodb
        :param form: Form
        :return: int - id new form
        """

        appLogger.info('create_form', 'form:', form.to_dict())
        form_id = cls._db[FORM_DOCUMENT].insert_one(form.to_dict())

        return form_id

    @classmethod
    def get_all(
            cls,
            all_fields: Dict[str, str]
    ) -> List[Dict[str, str]]:
        """
        Method for get forms much name field and type field
        :param all_fields: Dict[str, str] - dict of all fields
        :return: List[Dict[str, str]] | NotFoundForm - list of forms from mongodb
        """

        collections = cls._db[FORM_DOCUMENT]
        mongo_forms = list(collections.find({}))
        appLogger.info('get_all', 'mongo_forms:', mongo_forms, "all_fields:", all_fields)

        return mongo_forms

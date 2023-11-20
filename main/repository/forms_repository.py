from typing import Dict, List

from pymongo.collection import Collection

from main.logger import appLogger
from main.models.form import Form
from main.repository.interfaces.i_forms_repository import ReposForms


class FormsMongoRepository(ReposForms):
    """
    Class for work with database (work with forms).
    """

    _instance = None
    _collections: Collection = None

    def __new__(cls, collections: Collection, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super(FormsMongoRepository, cls).__new__(cls, *args, **kwargs)

        cls._collections = collections

        return cls._instance

    @classmethod
    def create_form(cls, form: Form) -> str:
        """
        method for create new form in mongodb
        :param form: Form
        :return: int - id new form
        """

        appLogger.info('create_form', 'form:', form.to_dict())
        form_id = cls._collections.insert_one(form.to_dict())

        return str(form_id.inserted_id)

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

        mongo_forms = list(cls._collections.find({}))
        appLogger.info('get_all', 'mongo_forms:', mongo_forms, "all_fields:", all_fields)

        return mongo_forms

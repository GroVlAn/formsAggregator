from typing import List, Dict, Optional

from main.logger import appLogger
from main.models.field import Field
from main.models.form import Form
from main.repository.interfaces.i_forms_repository import ReposForms
from main.services.interfaces.i_forms_service import FormsServicer
from main.tools.type_definition import type_definition
from main.types.field_types import EFieldTypes


class FormsService(FormsServicer):
    """
    Service for work with forms
    :param repos: ReposForms - forms repository
    """

    def __init__(self, repos: ReposForms):
        self.repos = repos

    @staticmethod
    def create_fields_list(init_data: Dict[str, str]) -> List[Field]:
        """
        method for create list of field form
        :param init_data: Dict[str, str] - data from response
        :return: List[Field]
        """

        fields = [Field(key, type_definition(value)) for key, value in init_data.items()]
        appLogger.info('create_fields_list', 'fields:', fields)

        return fields

    def find_forms(self, fields: List[Field]) -> Optional[List[Dict[str, str]]]:
        """
        method for get all forms by list fields
        :param fields: List[Field]
        :return: Optional[List[Dict[str, str]]]
        """

        all_fields = {field.name: EFieldTypes(field.type).value for field in fields}
        form = self.repos.get_all(all_fields=all_fields)

        if len(form) == 0:
            return None

        return [form for form in form if self._in_fields(form, all_fields)]

    def create_form(self, form: Form) -> int:
        """
        method for create new form
        :param form:
        :return:
        """

        id_form = self.repos.create_form(form)
        appLogger.info('create_form', 'form:', form.to_dict())

        return id_form

    @staticmethod
    def _in_fields(form: Dict[str, str], fields: Dict[str, str]) -> bool:
        copy_form = dict(form)

        del copy_form['_id']
        del copy_form['name']

        return all(key in fields.keys() and fields[key] == value for key, value in copy_form.items())

from abc import ABC, abstractmethod
from typing import List, Dict

from main.models.field import Field
from main.models.form import Form


class GetterForm(ABC):

    @abstractmethod
    def find_forms(self, fields: List[Field]) -> str:
        ...


class CreatorForm(ABC):

    @abstractmethod
    def create_form(self, form: Form) -> int:
        ...


class FinderTypes(ABC):

    @staticmethod
    @abstractmethod
    def create_fields_list(init_data: Dict[str, str]) -> List[Field]:
        ...


class FormsServicer(
    GetterForm,
    CreatorForm,
    FinderTypes,
):
    @abstractmethod
    def find_forms(self, fields: List[Field]) -> str:
        pass

    @abstractmethod
    def create_form(self, form: Form) -> int:
        pass

    @staticmethod
    @abstractmethod
    def create_fields_list(init_data: Dict[str, str]) -> List[Field]:
        pass

    ...

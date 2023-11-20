from abc import ABC, abstractmethod
from typing import Dict, List

from main.models.form import Form


class CreatorForm(ABC):

    @classmethod
    @abstractmethod
    def create_form(cls, form: Form) -> str:
        ...


class GetterForm(ABC):

    @classmethod
    @abstractmethod
    def get_all(
            cls,
            all_fields: Dict[str, str]
    ) -> List[Dict[str, str]]:
        ...


class ReposForms(
    CreatorForm,
    GetterForm,
    ABC
):
    ...

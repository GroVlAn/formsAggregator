from dataclasses import dataclass
from typing import List

from main.models.field import Field


@dataclass(frozen=True)
class Form:
    name: str
    fields: List[Field]

    def to_dict(self):

        form_dict = {'name': self.name}
        fields = {field.name: field.type for field in self.fields}
        form_dict.update(fields)

        return form_dict

import re
import time

from main.types.field_types import EFieldTypes


def _check_email(value: str) -> bool:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    return True if re.fullmatch(pattern, value) else False


def _check_phone(value: str) -> bool:
    pattern = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'

    return True if re.fullmatch(pattern, value) else False


def _check_date(value: str) -> bool:
    try:
        valid_date = time.strptime(value, '%d.%m.%Y')
        return True
    except ValueError:
        try:
            valid_date = time.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            return False


def type_definition(value: str) -> str:

    if _check_email(value):
        return EFieldTypes.EMAIL.value

    if _check_phone(value):
        return EFieldTypes.PHONE.value

    if _check_date(value):
        return EFieldTypes.DATE.value

    return EFieldTypes.TEXT.value

import re
from datetime import datetime

import errors


class Field:

    def __init__(self, value) -> None:
        self._value = None  # Private not Hidden!!!
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value) -> None:
        self._value = value


class Birthday(Field):

    @Field.value.setter
    def value(self, value: str = None) -> None:  # dd-mm-yyyy -> %d-%m-%Y
        if re.match(r"[a-zA-Z]{1}[\w.]{1,}@[a-zA-Z]{2,}.[a-zA-Z]{2,}", value):
            try:
                self._value = datetime.strptime(value, '%d-%m-%Y')  # raise ValueError if wrong
            except ValueError:
                raise errors.WrongBirthday('Data should be in format dd-mm-yyyy')

    def __str__(self):
        return self.value.strftime('%d-%m-%Y')


class Email(Field):

    @Field.value.setter
    def value(self, value: str) -> None:

        if '@' in value:
            self._value = value

        else:
            raise errors.WrongEmail(f"Looks like {value} is a wrong email")

    def __str__(self) -> str:
        return self.value


class Name(Field):

    @Field.value.setter
    def value(self, value: str) -> None:
        self._value = value

    def __str__(self) -> str:
        return self.value.title()


class Phone(Field):

    @Field.value.setter
    def value(self, value: str) -> None:

        if len(value) == 10 and value.isdigit():
            self._value = value

        else:
            raise errors.WrongNumber(f"Looks like {value} is a wrong number. It must be 10 digits")

    def __str__(self):
        return f"+38({self.value[:3]}){self.value[3:6]}-{self.value[6:8]}-{self.value[8:]}"  # +38(012)34-567-89
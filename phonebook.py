from collections import UserDict
from datetime import datetime
import re

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

        try:
            self._value = datetime.strptime(
                value, '%d-%m-%Y')  # raise ValueError if wrong
        except ValueError:
            raise errors.WrongBirthday('Data should be in format dd-mm-yyyy')

    def __str__(self):
        return self.value.strftime('%d-%m-%Y')


class Email(Field):

    @Field.value.setter
    def value(self, value: str) -> None:

        if re.match(r"[a-zA-Z][\w.]+@[a-zA-Z]{2,}.[a-zA-Z]{2,}.[a-zA-Z]{2,}$", value):
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
            raise errors.WrongPhone(
                f"Looks like {value} is a wrong number. It must be 10 digits")

    def __str__(self):
        # +38(012)34-567-89
        return f"+38({self.value[:3]}){self.value[3:6]}-{self.value[6:8]}-{self.value[8:]}"


class Record:

    def __init__(self, name: Name, phones: Phone = [], birthday: Birthday = None, emails=[]):
        self.name = name
        self.phones = [phones] if phones is not None else[]
        self.birthday = birthday
        self.emails = [emails] if emails is not None else[]

    def add_phone(self, phone):
        self.phones.append(phone)

    def change_phone(self, old_phone, new_phone):
        try:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)
        except ValueError:
            return f"{old_phone} does not exist"

    def delete_phone(self, phone):
        try:
            self.phones.remove(phone)
        except ValueError:
            return f"{phone} does not exists"

    def add_email(self, email):
        self.emails.append(email)

    def change_email(self, old_email, new_email):
        try:
            self.emails.remove(old_email)
            self.emails.append(new_email)
        except ValueError:
            return f"{old_email} does not exist"

    def delete_email(self, email):
        try:
            self.emails.remove(email)
        except ValueError:
            return f"{email} does not exists"


class AddressBook(UserDict):
    pass


class Notes:
    pass

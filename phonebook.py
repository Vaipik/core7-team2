from collections import UserDict
from datetime import datetime
import re
from typing import List, Optional

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
    """
    Contact record
    Attributes: name, birthday, emails,  phones, birthday, emails
    """

    def __init__(self, name: Name, phones: Optional[List[Phone]] = None,
                 birthday: Optional[Birthday] = None, emails: Optional[List[Email]] = None) -> None:
        self.name = name
        self.phones = phones
        self.birthday = birthday
        self.emails = emails

    def add_phone(self, phone: Phone) -> None:
        """
        Adding new phone to current record
        :param phone: instance of Phone
        :return: None
        """
        if self.phones is None:
            self.phones = [phone]
        else:
            self.phones.append(phone)
        return "Phone number added"

    def change_phone(self, old_phone: str, new_phone: Phone) -> str | None:
        """
        Changing user phone
        :param old_phone: phone to be changed
        :param new_phone: instance of Phone
        :return: string if no phone to be changed was found else None
        """
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone.value)
                self.phones.append(new_phone)
                return "Phone number changed"
            else:
                return f"{old_phone} does not exist"

    def delete_phone(self, phone_to_delete: str) -> str | None:
        """
        Deleting phone
        :param phone_to_delete: phone to be deleted
        :return: string if no phone was found else None
        """
        for phone in self.phones:
            if phone.value == phone_to_delete:
                self.phones.remove(phone.value)
                return "Phone number deleted"
            else:
                return f"{phone_to_delete} does not exist"

    def add_email(self, email: Email) -> None:
        """
        Adds new email to current record
        :param email: instance of Email
        :return: None
        """
        if self.emails is None:
            self.emails = [email]
        else:
            self.emails.append(email)
        return "Email added"

    def change_email(self, old_email: str, new_email: Email) -> str | None:
        """
        Changing user email
        :param old_email: email to be changed
        :param new_email: instance of Email
        :return: string if no email to be changed was found else None
        """
        for email in self.emails:
            if email.value == old_email:
                self.emails.remove(email.value)
                self.emails.append(new_email)
                return "Email changed"
        else:
            return f"{old_email} does not exist"

    def delete_email(self, email_to_delete: str) -> str | None:
        """
        Deleting email
        :param email_to_delete: email to be deleted
        :return: string if no email was found else None
        """
        for email in self.emails:
            if email.value == email_to_delete:
                self.emails.remove(email.value)
                return "Email deleted"
        else:
            return f"{email_to_delete} does not exist"


class AddressBook(UserDict):
    pass


class Notes:
    pass

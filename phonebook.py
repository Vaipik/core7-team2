from collections import UserDict
from datetime import datetime, timedelta
import re
from typing import Optional, List

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
                value, '%d-%m-%Y').date()  # raise ValueError if wrong
        except ValueError:
            raise errors.WrongBirthday('Data should be in format dd-mm-yyyy')

    def __str__(self):
        return self.value.strftime('%d-%m-%Y')


class Email(Field):

    @Field.value.setter
    def value(self, value: str) -> None:
        __pattern = r"^[a-zA-Z][\w.]{1,}@([a-zA-Z]{2,}[.][a-zA-Z]{2,}|[a-zA-Z]{2,}[.][a-zA-Z]{2,}[.][a-zA-Z]{2,})$"
        if re.match(__pattern, value):
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
    Attributes: name, phones, birthday, emails
    """

    def __init__(self, name: Name, phones: Optional[List[Phone]] = None,
                 birthday: Optional[Birthday] = None, emails: Optional[List[Email]] = None) -> None:
        self.name = name
        self.phones = phones
        self.birthday = birthday
        self.emails = emails

    def add_phone(self, phone: Phone) -> str:
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

    def change_phone(self, old_phone: str, new_phone: Phone) -> str:
        """
        Changing user phone
        :param old_phone: phone to be changed
        :param new_phone: instance of Phone
        :return: string if no phone to be changed was found
        """
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone.value)
                self.phones.append(new_phone)
                return "Phone number changed"
            else:
                return f"{old_phone} does not exist"

    def delete_phone(self, phone_to_delete: str) -> str:
        """
        Deleting phone
        :param phone_to_delete: phone to be deleted
        :return: string if no phone was found
        """
        for phone in self.phones:
            if phone.value == phone_to_delete:
                self.phones.remove(phone.value)
                return "Phone number deleted"
            else:
                return f"{phone_to_delete} does not exist"

    def add_email(self, email: Email) -> str:
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

    def change_email(self, old_email: str, new_email: Email) -> str:
        """
        Changing user email
        :param old_email: email to be changed
        :param new_email: instance of Email
        :return: string if no email to be changed was found
        """
        for email in self.emails:
            if email.value == old_email:
                self.emails.remove(email.value)
                self.emails.append(new_email)
                return "Email changed"
        else:
            return f"{old_email} does not exist"

    def delete_email(self, email_to_delete: str) -> str:
        """
        Deleting email
        :param email_to_delete: email to be deleted
        :return: string if no email was found
        """
        for email in self.emails:
            if email.value == email_to_delete:
                self.emails.remove(email.value)
                return "Email deleted"
        else:
            return f"{email_to_delete} does not exist"

    def add_birthday(self, birthday: Birthday) -> str:
        """
        Adding new birthday to current record
        :param birthday: instance of Birthday
        :return: None
        """
        if self.birthday is None:
            self.birthday = [birthday]
        else:
            return "Birthday exists"
        return "Birthday added"

    def change_birthday(self, old_birthday: str, new_birthday: Birthday) -> str:
        """
        Changing user birthday
        :param old_birthday: birthday to be changed
        :param new_birthday: instance of Birthday
        :return: string if no birthday to be changed was found
        """
        if self.birthday == old_birthday:
            self.birthday = new_birthday
            return "Birthday canged"
        else:
            return "Birthday does not exist"

    def delete_birthday(self, birthday_to_delete: Birthday) -> str:
        """
        Deleting birthday
        :param birthday_to_delete: birthday to be deleted
        :return: string if no birthday was found
        """
        if self.birthday == birthday_to_delete:
            self.birthday = None
            return "Birthday deleted"
        else:
            return "Birthday does not exist"

    def __len__(self):
        pass


class AddressBook(UserDict):

    __fields = ('name', 'birthday', 'emails', 'phones')

    def add_contact(self, record: Record) -> None:
        """
        Create new contact in phonebook

        :param record: Record instance with contact information
        :raise ContactExists: if contact is phonebook
        :return: None
        """
        contact = record.name.value
        if contact in self.data:
            raise errors.ContactExists(
                f"{contact} is already in your contacts")

        self.data[contact] = record

    # @decorator -> KeyError
    def delete_contact(self, contact: str) -> str:
        """
        Delete contact from phonebook

        :param contact: contact name to be deleted
        :return: Message if contact was deleted
        """
        if contact not in self.data:
            raise KeyError(f"{contact} is not in your phonebook")

        self.data.pop(contact)
        return f"{contact} has been deleted"

    def find_record(self, search: str) -> str | dict[list]:
        """
        Show records with similar or exact data
        :param search: information to search
        :return: None
        """
        if not search:
            raise errors.EmptySearchString

        _matched_information = {}
        for record in self.data.values():  # type: Record
            __information = []
            for field in AddressBook.__fields:

                record_field = getattr(record, field)
                if record_field is None:
                    continue

                # type: List[Phone], List[Email]
                if isinstance(record_field, list):
                    for data in record_field:
                        if search in data.value:
                            __information.append(data.value)

                elif isinstance(record_field, Birthday):  # type: Birthday
                    if search in record_field.value.strftime('%d-%m-%Y'):
                        __information.append(
                            record_field.value.strftime('%d-%m-%Y'))
                elif isinstance(record_field, Name):
                    if search in record_field.value:  # type: Name
                        __information.append(record_field.value)

            if __information:
                _matched_information[record.name.value] = __information.copy()
                __information.clear()

        return _matched_information

    def show_near_birthdays(self, days: int = 30) -> list:
        """
          Show users and their birthdays in given days

        :param days: days interval
        :return: None
        """
        current_date = datetime.now().date()
        birthdays = []

        for record in self.data.values():  # type: Record

            birthday = record.birthday.value.replace(year=current_date.year)
            if current_date <= birthday <= current_date + timedelta(days):
                birthdays.append(
                    f"{record.name.value} has birthday  {record.birthday.value.strftime('%d %B')}"
                    f" in {(birthday - current_date).days} days"
                )

        return birthdays


class Notes:
    pass

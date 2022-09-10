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
            self._value = datetime.strptime(value, '%d-%m-%Y').date()  # raise ValueError if wrong
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
            raise errors.WrongPhone(f"Looks like {value} is a wrong number. It must be 10 digits")

    def __str__(self):
        return f"+38({self.value[:3]}){self.value[3:6]}-{self.value[6:8]}-{self.value[8:]}"  # +38(012)34-567-89


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

    def add_email(self, email: Email) -> None:
        """
        Adds new email to current record

        :param email: instance of Email
        :return: None
        """
        if self.emails is None:
            self.emails = [email]
        self.emails.append(email)

    def add_phone(self, phone: Phone) -> None:
        """
        Adds new phone to current record

        :param phone: instance of Phone
        :return: None
        """
        if self.phones is None:
            self.phones = [phone]
        self.phones.append(phone)

    def change_email(self, old_email: str, new_email: Email) -> str | None:

        for email in self.emails:

            if email.value == old_email:
                self.emails.remove(email.value)
                self.emails.append(new_email)

        else:
            return f"{old_email} does not exist"

    def change_phone(self, old_phone: str, new_phone: Phone) -> str | None:

        for phone in self.phones:

            if phone.value == old_phone:

                self.phones.remove(phone.value)
                self.phones.append(new_phone)

        else:
            return f"{old_phone} does not exist"

    def delete_email(self, email_to_delete: str) -> str | None:

        for email in self.emails:
            if email.value == email_to_delete:
                self.emails.remove(email.value)
        else:
            return f"{email_to_delete} does not exist"

    def delete_phone(self, phone_to_delete: str) -> str | None:

        for phone in self.phones:
            if phone.value == phone:
                self.phones.remove(phone.value)
        else:
            return f"{phone_to_delete} does not exist"


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
            raise errors.ContactExists(f"{contact} is already in your contacts")

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

                if isinstance(record_field, list):  # type: List[Phone], List[Email]
                    for data in record_field:
                        if search in data.value:
                            __information.append(data.value)

                elif isinstance(record_field, Birthday):  # type: Birthday
                    if search in record_field.value.strftime('%d-%m-%Y'):
                        __information.append(record_field.value.strftime('%d-%m-%Y'))
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



nickita = Record(Name('Nickita'), birthday=Birthday('12-09-1997'), phones=[Phone('0930341951')], emails=[Email('n.khylko@gmail.com'), Email('rafael4uk@gmail.com')])
nastia = Record(Name('Nastia'), birthday=Birthday('04-10-1996'), phones=[Phone('0634702563')], emails=[Email('n.korinchyk@gmail.com'), Email('nasturuca@ukr.net')])

AB = AddressBook()
AB.add_contact(nickita)
AB.add_contact(nastia)

AB.find_record('ick')
AB.find_record('063')
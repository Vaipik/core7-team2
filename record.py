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
        Adding new phone to current record

        :param phone: instance of Phone
        :return: None
        """
        if self.phones is None:
            self.phones = [phone]
        self.phones.append(phone)

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

        else:
            return f"{old_email} does not exist"

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

        else:
            return f"{old_phone} does not exist"

    def delete_email(self, email_to_delete: str) -> str | None:
        """
        Deleting email

        :param email_to_delete: email to be deleted
        :return: string if no email was found else None
        """
        for email in self.emails:
            if email.value == email_to_delete:
                self.emails.remove(email.value)
        else:
            return f"{email_to_delete} does not exist"

    def delete_phone(self, phone_to_delete: str) -> str | None:
        """
        Deleting phone

        :param phone_to_delete: phone to be deleted
        :return: string if no phone was found else None
        """
        for phone in self.phones:
            if phone.value == phone:
                self.phones.remove(phone.value)
        else:
            return f"{phone_to_delete} does not exist"

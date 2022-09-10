class Record:
    def __init__(self, name, phones=[], birthday=None, emails=[]) -> None:
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
        self.phones.remove(phone)

    def add_email(self, email):
        self.emails.append(email)

    def change_email(self, old_email, new_email):
        try:
            self.emails.remove(old_email)
            self.emails.append(new_email)
        except ValueError:
            return f"{old_email} does not exist"

    def delete_email(self, email):
        self.emails.remove(email)

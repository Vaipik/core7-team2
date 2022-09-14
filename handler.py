import errors
from error_handler import error_handler
from file_sorter import sorter
from phonebook import Name, Birthday, Email, Phone, Record, AddressBook
from notes import NotesBook, NotesCommands


@error_handler
def add_birthday(*args) -> None:  # Username birthday
    """
    Is used to add contact birthday
    :param args: Username birthday
    :return: None
    """
    name, birthday, *tail = args

    record: Record = AB.get(name)
    record.add_birthday(
        Birthday(birthday)
    )
    AB.changed_contact_data(record)


@error_handler
def add_email(*args):
    print('adding email func')


@error_handler
def add_phone(*args):
    print('adding phone func')


@error_handler
def add_note(*args):
    print('adding note func')


@error_handler
def edit_birthday(*args):
    # print('changing birthday func')
    """
    Is used to change contacts birthday
    :param args: Username birthday
    :return: None
    """
    name, new_birthday, *tail = args

    record: Record = AB.get(name)
    record.change_birthday(
        Birthday(new_birthday)
    )
    AB.changed_contact_data(record)


@error_handler
def edit_email(*args):
    # print('changing email func')
    """
    Is used to change contacts email
    :param args: Username old_email, new_email
    :return: None
    """
    name, old_email, new_email, *tail = args

    record: Record = AB.get(name)
    record.change_email(
        Email(old_email, new_email)
    )
    AB.changed_contact_data(record)


@error_handler
def edit_phone(*args):
    # print('changing phone func')
    """
    Is used to change contacts phone
    :param args: Username old_phone new_phone
    :return: None
    """
    name, old_phone, new_phone, *tail = args

    record: Record = AB.get(name)
    record.change_phone(
        Phone(old_phone, new_phone)
    )
    AB.changed_contact_data(record)


@error_handler
def edit_note(*args):
    print('changing note func')


@error_handler
def delete_birthday(*args):
    # print('deleting birthday func')
    """
    Is used to delete contacts birthsay
    :param args: Username birthday
    :return: None
    """
    name, birthday, *tail = args

    record: Record = AB.get(name)
    record.delete_birthday(
        Birthday(birthday)
    )
    AB.changed_contact_data(record)


@error_handler
def delete_email(*args):
    # print('deleting email func')
    """
    Is used to delete contacts email
    :param args: Username email
    :return: None
    """
    name, email, *tail = args

    record: Record = AB.get(name)
    record.delete_email(
        Email(email)
    )
    AB.changed_contact_data(record)


@error_handler
def delete_phone(*args):
    print('deleting phone func')
    """
    Is used to delete contacts phone
    :param args: Username phone
    :return: None
    """
    name, phone, *tail = args

    record: Record = AB.get(name)
    record.delete_phone(
        Phone(phone)
    )
    AB.changed_contact_data(record)


@error_handler
def delete_note(*args):
    print('deleting note func')


@error_handler
def new_contact(*args) -> None:  # Username .....
    """

    :param args: query
    :return: None
    """
    name = Name(args[0])
    # Simple check for email
    phones = [Phone(data) for data in args[1:] if data.isdigit()]
    # Simple check for email
    emails = [Email(data) for data in args[1:] if '@' in data]

    for data in args[1:]:
        birthday = Birthday(
            data) if '@' not in data and not data.isdigit() else None

    record = Record(name=name, birthday=birthday, emails=emails, phones=phones)
    AB.add_contact(record)


@error_handler
def change_phonebook(*args):
    print('changing phonebook func')


@error_handler
def change_notebook(*args):
    print('changing notebook func')


@error_handler
def find_note(*args):
    pass


@error_handler
def find_phonebook(*args):
    pass


@error_handler
def find_tag(*args):
    pass


@error_handler
def show_contacts(*args):
    pass


@error_handler
def show_help(*args):
    pass


@error_handler
def show_notes(*args):
    pass


@error_handler
def sort_folder(*args) -> None:
    """

    :param args:
    :return:
    """
    if len(args) != 1:
        raise ValueError
    sorter(args)


@error_handler
def sort_tag(*args):
    pass


@error_handler
def wrong_command(*args):

    input_command = f"{args[0]} {args[1]}"

    for d in OPERATIONS.keys():
        if input_command in d:
            return d

    return wrong_command(input_command[:-1])


def input_parser(user_input: str) -> list:
    user_input = user_input.split()
    return ['wrong', 'command'] if len(user_input) < 2 else user_input


OPERATIONS = {
    'add birthday': add_birthday,
    'add email': add_email,
    'add phone': add_phone,
    'add note': add_note,  # Vova
    'edit birthday': edit_birthday,  # Andrii
    'edit email': edit_email,  # Andrii
    'edit phone': edit_phone,  # Andrii
    'edit note': edit_note,  # Vova
    'delete birthday': delete_birthday,  # Andrii
    'delete email': delete_email,  # Andrii
    'delete phone': delete_phone,  # Andrii
    'delete note': delete_note,  # Vova
    'find tag': find_tag,  # Vova
    'find note': find_note,  # Vova
    'find phonebook': find_phonebook,
    'sort tag': sort_tag,  # Vova
    'show help': show_help,
    'show contacts': show_contacts,
    'show notes': show_notes,  # Vova
    'new contact': new_contact,
    'change phonebook': change_phonebook,
    'change notebook': change_notebook,
    'sort folder': sort_folder,
}


AB = AddressBook('tests')
NB = NotesBook()  # Vova
NBCmd = NotesCommands()  # Vova

while True:

    print(">>> Hello! I am your CLI helper. Please enter show help to see what can i do!")
    command, data_type, *query = input_parser(input())
    if command == 'stop':
        break
    action = OPERATIONS.get(command + ' ' + data_type, wrong_command)
    action(query)

# def handler

    # if __name__ == '__main__':
    #     # handler()

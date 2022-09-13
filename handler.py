import errors
from error_handler import error_handler
from file_sorter import sorter
from phonebook import Name, Birthday, Email, Phone, Record, AddressBook
from notes import NotesBook, NotesCommands


@error_handler
def add_birthday(*args) -> None:  # Username birthday
    """
    Is used to change contact birthday
    :param args: Username birthday
    :return: None
    """
    name, birthday, *tail = args

    record: Record = AB.get(name)
    record.change_birthday(
        Birthday(birthday)
    )
    AB.changed_contact_data(record)


@error_handler
def add_email(*args):
    name, email, *tail = args

    record: Record = AB.get(name)
    record.add_email(
        Email(email)
    )
    AB.changed_contact_data(record)


@error_handler
def add_phone(*args):
    name, phone, *tail = args

    record: Record = AB.get(name)
    record.add_phone(
        Phone(phone)
    )
    AB.changed_contact_data(record)


@error_handler
def add_note(*args):
    print('adding note func')


@error_handler
def edit_birthday(*args):
    print('changing birthday func')


@error_handler
def edit_email(*args):
    print('changing email func')


@error_handler
def edit_phone(*args):
    print('changing phone func')


@error_handler
def edit_note(*args):
    print('changing note func')


@error_handler
def delete_birthday(*args):
    print('deleting birthday func')


@error_handler
def delete_email(*args):
    print('deleting email func')


@error_handler
def delete_phone(*args):
    print('deleting phone func')


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
    phones = [Phone(data) for data in args[1:] if data.isdigit()]  # Simple check for email
    emails = [Email(data) for data in args[1:] if '@' in data]  # Simple check for email

    for data in args[1:]:
        birthday = Birthday(data) if '@' not in data and not data.isdigit() else None

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
    name = args
    print("""'add birthday' - add to your contact birthday date, format - dd-mm-yyyy,
    'add email'- add to your contact email address, format - example@gmail.com,
    'add phone'- add to your contact phone, format - 10 numbers,
    'add note'- add note to the notebook,  
    'edit birthday' - change already created birthday date, format - dd-mm-yyyy,
    'edit email'- change already created email address, format - example@gmail.com,
    'edit phone'- change already created phone number, format - 10 numbers,
    'edit note'- change already created note,  
    'delete birthday'- delete already created birthday date,
    'delete email'- delete already created email address,
    'delete phone'- delete already created phone number,
    'delete note'- delete already created note,  
    'find tag'- find tag from notebook,  
    'find note'- find note from notebook,  
    'find phonebook'- find phonebook,
    'sort tag'- sorted your tag,  
    'show help'- show information for all commands,
    'show contacts'- show all contacts,
    'show note'- show notes,  
    'new contact'- add new contact,
    'change phonebook'- change information in phonebook,
    'change notebook'- change information in notebook,
    'sort folder' - sorted all your file except phonebook and notebook""")

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
    'edit birthday': edit_birthday,
    'edit email': edit_email,
    'edit phone': edit_phone,
    'edit note': edit_note,  # Vova
    'delete birthday': delete_birthday,
    'delete email': delete_email,
    'delete phone': delete_phone,
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

    print(">>> Hello! I am your CLI helper. Please enter 'show help' to see what can i do!")
    command, data_type, *query = input_parser(input())
    if command == 'stop':
        break
    action = OPERATIONS.get(command + ' ' + data_type, wrong_command)
    action(query)

# def handler


    # if __name__ == '__main__':
    #     # handler()

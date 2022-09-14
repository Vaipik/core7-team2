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
    record: Record = AB[name]
    result = record.add_birthday(
        Birthday(birthday)
    )
    if 'exists' not in result:
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
def birthdays_in(*args) -> None:
    """
    Show birthday persons in given days\n
    :param args: days
    :return: None
    """
    days = int(args[0]) if args else None
    birthdays = AB.show_near_birthdays(days) if days else AB.show_near_birthdays()
    print(*birthdays)


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
    Adding new contact to your phonebook
    :param args: query
    :return: None
    """
    name = Name(args[0])
    record = Record(name)
    for arg in args[1:]:

        if arg.isdigit():
            record.add_phone(Phone(arg))

        elif '@' in arg:
            record.add_email(Email(arg))

        else:
            record.add_birthday(Birthday(arg))

    AB.add_contact(record)


@error_handler
def change_phonebook(*args):

    global AB
    AB = AddressBook(args[0])


@error_handler
def change_notebook(*args):
    print('changing notebook func')


@error_handler
def find_note(*args):
    pass


@error_handler
def find_phonebook(*args) -> None:

    information = [AB.find_record(arg) for arg in args]
    for answer in information:

        for username, fields in answer.items():

            if len(fields) == 1 and username == fields[0]:  # username is a key
                print(f"Looks like you are looking for {username} contact")
                # print(AB.show_contact(username))
            else:
                print(f"Looks like you are looking for {username} data:")
                for field in fields:
                    print(field[0], end=': ')
                    print(*field[1:], sep=', ')


@error_handler
def find_tag(*args):
    pass


@error_handler
def show_contact(*args) -> None:
    """
    Is used to show one exact contact data
    :param args:
    :return:
    """
    name = args[0]
    contact_info = AB.show_record_data(name)

    for field in contact_info:
        print(*field)


@error_handler
def show_contacts(*args) -> None:
    """
    Show all phonebook records separated on pages
    :param args: records per page
    :return:
    """
    records_per_page = int(args[0]) if args else None

    pages = AB.show_contacts(records_per_page) if records_per_page else AB.show_contacts()

    for page in pages:
        for data in page:
            print(*data)


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
        raise ValueError('Wrong path buddy')
    print(sorter(args[0]))


@error_handler
def sort_tag(*args):
    pass


@error_handler
def wrong_command(*args):

    input_command = f"{args[0]} {args[1]}"
    print(input_command)
    for d in OPERATIONS.keys():
        if input_command in d:
            print(d)
            return d
    return wrong_command(input_command[:-1])


def input_parser(user_input: str) -> list:
    """

    :param user_input:
    :return:
    """
    stop_word = ('stop', 'exit', 'goodbye')
    for word in stop_word:
        if word in user_input.lower():
            return ['break', []]

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
    'birthdays in': birthdays_in,
    'show contact': show_contact,
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
print(">>> Hello! I am your CLI helper. Please enter show help to see what can i do!")

while True:

    command, data_type, *query = input_parser(input())
    print(command, data_type)
    if command == 'break':
        break
    action = OPERATIONS.get(command + ' ' + data_type, wrong_command)
    if action.__name__ == 'wrong_command':
        action(command, data_type)
    else:
        if not query:
            query = []
        print(action(*query))

# def handler

    # if __name__ == '__main__':
    #     # handler()

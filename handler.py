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
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.add_birthday(
        Birthday(birthday)
    )
    if 'exists' not in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def add_email(*args):
    """
    Is used to change contact phone
    :param args: Username phone
    :return: None
    """
    name, email, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.add_email(
        Email(email)
    )
    if 'exists' not in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def add_phone(*args):
    """
    Is used to change contact phone
    :param args: Username phone
    :return: None
    """
    name, phone, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.add_phone(
        Phone(phone)
    )
    if 'exists' not in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def add_note(*args):
    name = input("Enter note name: ")
    tags = input("Enter tags for note: ")
    text = input("Enter note text: ")
    print(NBCmd.add_note(name, tags, text, NBCmd))


@error_handler
def birthdays_in(*args) -> None:
    """
    Show birthday persons in given days\n
    :param args: days
    :return: None
    """
    days = int(args[0]) if args else None
    birthdays = AB.show_near_birthdays(days) if days else AB.show_near_birthdays()
    print(*birthdays, sep='\n')


@error_handler
def edit_birthday(*args) -> None:
    """
    Changing birthday
    :param args: username new birthday date
    :return: None
    """
    name, new_birthday, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.change_birthday(
        Birthday(new_birthday)
    )
    if 'changed' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def edit_email(*args) -> None:
    """
    Is used to change contacts email
    :param args: Username old_email, new_email
    :return: None
    """
    name, old_email, new_email, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.change_email(
        old_email, Email(new_email)
    )
    if 'changed' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def edit_phone(*args):
    """
    Is used to change contacts phone
    :param args: Username old_phone new_phone
    :return: None
    """
    name, old_phone, new_phone, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.change_phone(
        old_phone, Phone(new_phone)
    )
    if 'changed' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def edit_note(*args):
    name = input("Enter the name of the note you want to edit: ")
    if name not in NB.data:
        raise KeyError(f'\033[33mNote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
    else:
        print(f"Old  text note: {NBCmd.get_note(name, NB)}")
        new_note = input("Edit text note: ")
        print(NBCmd.edit_note(name, new_note, NB))
   

@error_handler
def edit_tag(*args):                                        # area of responsibility Volodymyr
    name = input("Enter the name of the note where you want to edit tags: ")
    if name not in NB.data:
        raise KeyError(f'\033[33mNote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
    else:
        print(f"Old  tags: {', '.join(NBCmd.get_tags(name, NB))}")
        new_tags = input("Edit tags: ")
        print(NBCmd.edit_tags(name, new_tags, NB))        


@error_handler
def delete_birthday(*args):
    """
    Is used to delete contacts birthsay
    :param args: Username birthday
    :return: None
    """
    name, birthday, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.delete_birthday(
        Birthday(birthday)
    )
    if 'deleted' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def delete_email(*args):
    """
    Is used to delete contacts email
    :param args: Username email
    :return: None
    """
    name, email, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.delete_email(
        email
    )
    if 'deleted' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def delete_phone(*args):
    """
        Is used to delete contacts phone
        :param args: Username phone
        :return: None
        """
    name, phone, *tail = args

    record: Record = AB.get(name)
    if record is None:
        raise KeyError(f"{name} contact does not exist")

    result = record.delete_phone(
        phone
    )
    if 'deleted' in result:
        AB.changed_contact_data(record)
    print(result)


@error_handler
def delete_note(*args):
    name = input("Enter the name of the note you want to delete: ")
    confirm = input("Do you really want to delete y/n: ")
    if confirm.lower() == "y":
        print(NBCmd.delete_note(name, NB))


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
    request = input("Enter a query to search: ")
    print(NBCmd.find_note(request, NB))


@error_handler
def find_phonebook(*args) -> None:

    information = [AB.find_record(arg) for arg in args]
    for answer in information:

        for username, fields in answer.items():

            if len(fields) == 1 and username == fields[0]:  # username is a key
                print(f"Looks like you are looking for {username} contact")
            else:
                print(f"Looks like you are looking for {username} data:")
                for field in fields:
                    print(field[0], end=': ')
                    print(*field[1:], sep=', ')


@error_handler
def find_tag(*args):
    print(NBCmd.find_tag("available", NB))
    tag = input("Enter a tag: ")
    print(NBCmd.find_tag(tag, NB)) 


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
def show_note(*args):                                         # area of responsibility Volodymyr
    name = input("Enter the name of the note you want to view: ")
    print(NBCmd.show_some_note(name, NB))

    
@error_handler
def show_notes(*args):
    print(NBCmd.show_all_notes(NB))


@error_handler
def sort_folder(*args) -> None:
    """
    /home/nkhylko/IT/GoIT/module-6/trash UNIX
    :param args:
    :return:
    """
    if len(args) != 1:
        raise ValueError('Wrong path buddy')
    print(sorter(args[0]))


@error_handler
def sort_tag(*args):
    print(NBCmd.sort_tag(NB))


def suitable_command(input_command: str) -> str:

    for command in OPERATIONS. keys():
        if input_command in command:
            return command
    return suitable_command(input_command[:-1])


def wrong_command(*args):

    input_command = f"{args[0]} {args[1]}"
    print(f"Maybe you mean {suitable_command(input_command)}")


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
    'birthdays in': birthdays_in,
    'change phonebook': change_phonebook,
    'change notebook': change_notebook,
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
    'new contact': new_contact,
    'show contact': show_contact,
    'show contacts': show_contacts,
    'show help': show_help,
    'show notes': show_notes,  # Vova
    'sort folder': sort_folder,
    'sort tag': sort_tag,  # Vova
}

AB = AddressBook('tests')
NB = NotesBook()  # Vova
NBCmd = NotesCommands()  # Vova


def handler():

    while True:
        command, data_type, *query = input_parser(input())
        if command == 'break':
            break

        action = OPERATIONS.get(command + ' ' + data_type, wrong_command)
        if action.__name__ == 'wrong_command':
            action(command, data_type)

        else:

            if not query:
                query = []

            action(*query)

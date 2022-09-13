import phonebook
import notes


def main(address_book: phonebook.AddressBook):

        obj_note = notes.NotesCommands()
        # obj_name = phonebook.Name()
        # obj_email = phonebook.Record()
        # obj_birthday = phonebook.Record()
        # obj_phone = phonebook.Record()
        obj_contact = address_book

        while True:
            user_text = input()
            user_text = user_text.lower()
            if user_text == "hello":
                print("""How can I help you? 
If you don't know how names command, print 'show all command'""")
            elif user_text.startswith("add contact"):
                name = phonebook.Name(input("Enter name"))
                phone_numbers = []
                emails = []
                while True:
                    phone_numbers.append(phonebook.Phone(input("Enter phone: ")))
                    if input("Do you want to stop adding phone numbers? (y)") == "y":
                        break
                birthday = phonebook.Birthday(input("Enter a birthday date in format dd-mm-yyyy: "))
                while True:
                    emails.append(phonebook.Email(input("Enter email: ")))
                    if input("Do you want to stop adding emails? (y)") == "y":
                        break
                record = phonebook.Record(name=name, phones=phone_numbers, birthday=birthday, emails=emails)
                obj_contact.add_contact(record)
            # elif user_text.startswith("add email"):
            #     obj_phone = user_text.startswith("add email")
            #     obj_phone.phonebook.Record.add_email()
            # elif user_text.startswith("add birthday"):
            #     obj_phone = user_text.startswith("add birthday")
            #     obj_phone.phonebook.Record.add_birthday()
            # elif user_text.startswith("add name"):
            #     obj_phone = user_text.startswith("add name")
            #     obj_phone.phonebook.Record.add_phone()
            elif user_text.startswith("add notes"):
                note_tag = input("Enter tag: ")
                note = input("Enter note text")
                if note != "":
                    obj_note.add_note(note_tag, note)
                else:
                    obj_note.add_note(note_tag)
                # obj_note.notes.NotesCommands.add_note()
            elif user_text.startswith("change phone"):
                phone = phonebook.Phone(input())
            elif user_text.startswith("change email"):
                obj_phone = user_text.startswith("change email")
                obj_phone.phonebook.Record.change_email()
            elif user_text.startswith("change birthday"):
                obj_phone = user_text.startswith("change birthday")
                obj_phone.phonebook.Record.change_birthday()
            elif user_text.startswith("change name"):
                obj_phone = user_text.startswith("change name")
                obj_phone.phonebook.Name.change_name()
            elif user_text.startswith("change notes"):
                note_tag = input("Enter tag: ")
                note = input("Enter note text")
                if note != "":
                    obj_note.edit_note(note_tag, note)
                else:
                    obj_note.edit_note(note_tag)
            # elif user_text.startswith("delete name "):

            # elif user_text.startswith("delete phone "):
            #
            # elif user_text.startswith("delete email "):
            #
            # elif user_text.startswith(" delete birthday "):
            #
            # elif user_text.startswith(" delete notes "):
            #     note_tag = input("Enter tag: ")
            #     obj_note.delete_note(note_tag)
            elif user_text.startswith("show all contacts"):
                # obj_phone = user_text.startswith("show all contacts")
                obj_contact.show_contacts()
                # :param
                # user_input: fields to be shown on one page
                # :return: None

                # fields_per_page не обов'язковий параметр
                for page in address_book.show_contacts():
                    for elem in page:
                        print(elem[0], end=' ')  # field name
                        print(*elem[1:], sep=', ')  # field information
            # elif user_text.startswith("show all phones"):
            #     obj_phone = user_text.startswith("show all phones")
            #     obj_phone.phonebook.Record.
            # elif user_text.startswith("show all emails"):
            #     obj_phone = user_text.startswith("show all emails")
            #     obj_phone.phonebook.Record.change_birthday()
            #
            elif user_text.startswith("show all notes"):
                obj_note.show_all_notes()
            # elif user_text.startswith("show all birthday"):
            #     obj_phone = user_text.startswith("show all birthday")
            #     obj_phone.phonebook.Record.change_birthday()

            elif user_text.startswith("good bye ") or user_text.startswith("close") or user_text.startswith(
                    "exit") or user_text.startswith("."):
                print("Good bye!")
                break


AB = phonebook.AddressBook()

main(AB)

from collections import UserDict
from datetime import datetime
import pickle


class NotesBook(UserDict):
    def __init__(self):
        self.filename = "notesbook.txt"
        self.data = {}

    def read_file(self) -> None:
        try:
            with open(self.filename, 'rb') as fh:
                unpacked = pickle.load(fh)
                self.data = unpacked
        except FileNotFoundError:
            self.data = {}

    def save_in_file(self) -> None:
        with open(self.filename, 'wb') as fh:
            pickle.dump(self.data, fh)


class NotesCommands(NotesBook):

    def add_note(self, name: str, tags: str, note: str, notesbook: NotesBook) -> None:
        """the function of adding a new note"""
        notesbook.read_file()
        create = datetime.now()
        if name not in notesbook.data:   
            list_tags = []
            for i in tags.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('  ', ' ').split(' '):
                list_tags.append(i)
            note_data = {"tags": list_tags, "create": create.strftime("%d.%m.%Y %H:%M"), "note": note}
            notesbook.data[name] = note_data
            notesbook.save_in_file()
        else:
            print(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m exists, if you want to change it enter the command: edit note\033[37m')

    def delete_note(self, name: str, notesbook: NotesBook) -> None:
        """function to delete a note"""
        notesbook.read_file()
        if name not in notesbook.data:
            print(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            del notesbook.data[name]
            notesbook.save_in_file()

    def edit_note(self, name: str, note: str, notesbook: NotesBook) -> None:
        """note editing function"""
        notesbook.read_file()
        if name not in notesbook.data:
            print(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            notesbook.data[name]["note"] = note
            notesbook.save_in_file()

    def get_note(self, name: str,  notesbook: NotesBook) -> str:
        """a service function for outputting the content of a note, for example, for editing the text of a note so that the old content is visible"""
        notesbook.read_file()
        return notesbook.data[name]["note"]

    def edit_tags(self, name: str, tags: str, notesbook: NotesBook) -> None:
        """function of editing tags in a note"""
        notesbook.read_file()
        if name not in notesbook.data:
            print(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            list_tags = []
            for i in tags.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('  ', ' ').split(' '):
                list_tags.append(i)
            notesbook.data[name]["tags"] = list_tags
            notesbook.save_in_file()

    def get_tags(self, name: str,  notesbook: NotesBook) -> str:
        """a service function for outputting the tags of a note, for example, for editing the tags of a note so that the old content is visible"""
        notesbook.read_file()
        return notesbook.data[name]["tags"]    

    def show_some_note(self, name: str,  notesbook: NotesBook) -> str:
        """function to display some note"""
        notesbook.read_file()
        if name not in notesbook.data:
            print(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            result = f'''\n  name:  {name}\n  tags:  {", ".join(notesbook.data[name]["tags"])}\ncreate:  {notesbook.data[name]["create"]}\n  note:  {notesbook.data[name]["note"]}\n'''
            print(result)
            return result

    def show_all_notes(self, notesbook: NotesBook) -> str:
        """function to display all notes"""
        notesbook.read_file()
        result = "\033[32m\n*** ALL YOUR NOTES ***\033[0m\n"
        for k, v in notesbook.data.items():
            result += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        print(result)
        return result

    def find_note(self, request: str, notesbook: NotesBook) -> str:
        """function to search for a note by title or content"""
        notesbook.read_file()
        find = ""
        for k, v in notesbook.data.items():
            if (request.lower() in k.lower()) or (request.lower() in v["note"].lower()):
                find += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        if find == "":
            print('\033[33m*** No notes found for your request ***\033[0m')
        else:
            result = "\033[32m\n*** FIND NEXT NOTES ***\n\033[0m" + find
            print(result)
            return result

    def find_tag(self, tag: str, notesbook: NotesBook) -> str:
        """function to search for a note by tag"""
        notesbook.read_file()
        find = ""
        all_tags = []
        for k, v in notesbook.data.items():
            all_tags.extend(v["tags"])
            if (tag.lower() in v["tags"]) or (tag in v["tags"]):
                find += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        available = ', '.join(set(all_tags))
        if tag == "available":
            print("\nIn all your Notes are available next tags :\n" + available + "\n")
        elif find == "":
            print(f'\033[33m*** No notes found with tag \033[43m {tag} \033[0m\033[33m ***\033[0m')
        else:
            result = f"\033[32m\n*** Find next notes with tag \033[42m {tag} \033[0m\033[32m ***\n\033[0m" + find
            print(result)
            return result
    
    def sort_tag(self, notesbook: NotesBook) -> str:
        """function to display all notes sorted by tags alphabetically"""
        notesbook.read_file()
        result = ""
        all_tags = []
        for k, v in notesbook.data.items():
            all_tags.extend(v["tags"])
        for n in sorted(set(all_tags)):
            result += f"\033[4mNotes with tag {n}:\033[0m\n"
            for k, v in notesbook.data.items():
                if (n.lower() in v["tags"]) or (n in v["tags"]):
                    result += f'''  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        print(result)
        return result
       

# # НАСТУПНИЙ КОД ТІЛЬКИ ДЛЯ ПЕРЕВІРКИ ОКРЕМОГО ФУНКЦІОНУВАННЯ РОБОТИ З НОТАТКАМИ 

# notescommands = NotesCommands()

# welcome = """ДОСТУПНІ КОМАНДИ:
# new note - команда додавання нового нотатка (після введення команди спочатку запросить назву нотатка, потім сам текст нотатка)
# delete note - команда видалення нотатка
# edit note - команта редагування нотатка
# edit tags - команта редагування тегів нотатка
# all notes - відобразити всі створені нотатки
# note - команда відображення певного нотатка (після введення команди спочатку запросить назву нотатка, потім виведе текст нотатка)
# find note - пошук нотатка по назві або тексту
# find tag - пошук нотатка по тегу
# sort tag - команда що виводить нотатки згідно сортованих по алфавіту тегам
# stop - вихід з циклу Бота
# """
# print('\033[32m\n*** start a mini CLI-bot (only for test notes) ***\n\033[0m')
# print(welcome)
# while True:

#     userinput = input(": ")
#     if userinput.lstrip().lower() == "stop":
#         print('\033[32m*** mini CLI-bot end of work (only for test notes) ***\n\033[0m')
#         break

#     elif userinput.lstrip().lower() == "new note":
#         name = input(": enter note name: ")
#         tags = input(": enter tags for note: ")
#         text = input(": enter note text: ")
#         notescommands.add_note(name, tags, text, NotesBook())

#     elif userinput.lstrip()[0:11].lower() == "delete note":
#         name = input(": name of the note you want to delete: ")
#         confirm = input(": do you really want to delete y/n: ")
#         if confirm.lower() == "y":
#             notescommands.delete_note(name, NotesBook())

#     elif userinput.lstrip()[0:9].lower() == "edit note":
#         name = input(": name of the note you want to edit: ")
#         try:
#             print(f": old  text note: {notescommands.get_note(name, NotesBook())}")
#             new_note = input(": edit text note: ")
#             notescommands.edit_note(name, new_note, NotesBook())
#         except KeyError:
#             print(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')

#     elif userinput.lstrip()[0:8].lower() == "edit tag":
#         name = input(": name of the note where you want to edit tags: ")
#         try:
#             print(f": old  tags: {', '.join(notescommands.get_tags(name, NotesBook()))}")
#             new_tags = input(": edit tags: ")
#             notescommands.edit_tags(name, new_tags, NotesBook())
#         except KeyError:
#             print(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')

#     elif (userinput.lstrip().lower() == "all notes") or (userinput.lstrip().lower() == "all note"):
#         notescommands.show_all_notes(NotesBook())

#     elif userinput.lstrip().lower() == "note":
#         name = input(": enter the name of the note you want to view: ")
#         notescommands.show_some_note(name, NotesBook())

#     elif userinput.lstrip().lower() == "find note":
#         request = input(": enter a query to search: ")
#         notescommands.find_note(request, NotesBook())       
    
#     elif userinput.lstrip().lower() == "find tag":
#         notescommands.find_tag("available", NotesBook())
#         tag = input(": enter a tag: ")
#         notescommands.find_tag(tag, NotesBook())  

#     elif userinput.lstrip().lower() == "sort tag":
#         notescommands.sort_tag(NotesBook()) 

# # python3 notes.py
from collections import UserDict
from datetime import datetime
from pathlib import Path
import pickle


class NotesBook(UserDict):

    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR.joinpath('data')
    def __init__(self):

        self.filename = NotesBook.DATA_DIR.joinpath('notesbook.note')
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


class NotesCommands():

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
            return (f'Note with name \033[47m\033[30m {name} \033[0m successfully added.')
        else:
            return (f'\033[33mNote with name \033[43m {name} \033[0m\033[33m exists, if you want to change it enter the command: edit note\033[0m')

    def delete_note(self, name: str, notesbook: NotesBook) -> None:
        """function to delete a note"""
        notesbook.read_file()
        if name not in notesbook.data:
            return (f'\033[33mNote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            del notesbook.data[name]
            notesbook.save_in_file()
            return (f'Note with name \033[47m\033[30m {name} \033[0m deleted.')

    def edit_note(self, name: str, note: str, notesbook: NotesBook) -> None:
        """note editing function"""
        notesbook.read_file()
        if name not in notesbook.data:
            return (f'\033[33mNote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            notesbook.data[name]["note"] = note
            notesbook.save_in_file()
            return (f'Note with name \033[47m\033[30m {name} \033[0m edited.')

    def get_note(self, name: str,  notesbook: NotesBook) -> str:
        """a service function for outputting the content of a note, for example, for editing the text of a note so that the old content is visible"""
        notesbook.read_file()
        return notesbook.data[name]["note"]

    def edit_tags(self, name: str, tags: str, notesbook: NotesBook) -> None:
        """function of editing tags in a note"""
        notesbook.read_file()
        if name not in notesbook.data:
            return (f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            list_tags = []
            for i in tags.replace('.', ' ').replace(',', ' ').replace(';', ' ').replace('  ', ' ').split(' '):
                list_tags.append(i)
            notesbook.data[name]["tags"] = list_tags
            notesbook.save_in_file()
            return (f'Tags in note \033[47m\033[30m {name} \033[0m edited.')

    def get_tags(self, name: str,  notesbook: NotesBook) -> str:
        """a service function for outputting the tags of a note, for example, for editing the tags of a note so that the old content is visible"""
        notesbook.read_file()
        return notesbook.data[name]["tags"]    

    def show_some_note(self, name: str,  notesbook: NotesBook) -> str:
        """function to display some note"""
        notesbook.read_file()
        if name not in notesbook.data:
            return(f'\033[33mnote with name \033[43m {name} \033[0m\033[33m does not find\033[0m')
        else:
            result = f'''\n  name:  {name}\n  tags:  {", ".join(notesbook.data[name]["tags"])}\ncreate:  {notesbook.data[name]["create"]}\n  note:  {notesbook.data[name]["note"]}\n'''
            return result

    def show_all_notes(self, notesbook: NotesBook) -> str:
        """function to display all notes"""
        notesbook.read_file()
        result = "\033[32m\n*** ALL YOUR NOTES ***\033[0m\n"
        for k, v in notesbook.data.items():
            result += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        return result

    def find_note(self, request: str, notesbook: NotesBook) -> str:
        """function to search for a note by title or content"""
        notesbook.read_file()
        find = ""
        for k, v in notesbook.data.items():
            if (request.lower() in k.lower()) or (request.lower() in v["note"].lower()):
                find += f'''\n  name:  {k}\n  tags:  {", ".join(v["tags"])}\ncreate:  {v["create"]}\n  note:  {v["note"]}\n'''
        if find == "":
            return ('\033[33m*** No notes found for your request ***\033[0m')
        else:
            result = "\033[32m\n*** FIND NEXT NOTES ***\n\033[0m" + find
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
            return("\nIn all your Notes are available next tags :\n" + available + "\n")
        elif find == "":
            return(f'\033[33m*** No notes found with tag \033[43m {tag} \033[0m\033[33m ***\033[0m')
        else:
            result = f"\033[32m\n*** Find next notes with tag \033[42m {tag} \033[0m\033[32m ***\n\033[0m" + find
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
        return result

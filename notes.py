from collections import UserDict
from datetime import datetime

class NotesBook(UserDict):
    def __init__(self):
        self.filename = "notes.csv"
        self.data = {}



class NotesCommands:

    def add_note(self, teg: str, note = "* empty note *"):

        create = datetime.now()

        if teg not in notesbook.data:   
            all_note_data = {"create": [create.strftime("%d.%m.%Y %H:%M")], "note": note}
            notesbook.data[teg] = all_note_data
        else:
            return '**  a note with this name exists, if you want to change it enter the command: edit note  **'


        print(notesbook.data)


        return '** note added successfully **'


    
notesbook = NotesBook()
notescommands = NotesCommands()
notescommands.add_note("list for buy", "solt, oil, 10 eggs, bread, 2l milk")

# python3 notes.py
# Можливо повинен мати два поля
# Список для простих нотатків
# Словник із вкладеним списком(словником) для записів по тегам

# add_note(text: str) -> None:
# add_tagged_note(tag: str, text:str) - > None
# delete_note(text: str) -> None
# delete_tagged_note(tag: str) -> None
# edit_note(old_text: str, new_text) -> None
# edit_tagged_note(tag: str, old_text: str, new_text: str) -> None
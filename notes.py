from collections import UserDict
from datetime import datetime
import csv


class NotesBook(UserDict):
    def __init__(self):
        self.filename = "notesbook.csv"
        self.data = {}

    def read_file(self):
        try:
            with open(self.filename, 'r') as fh:
                reader = csv.DictReader(fh, delimiter=',')
                for row in reader:
                    self.data[row['tag']]={'create': row['create'], 'note': row['note']}
        except FileNotFoundError:
            self.data = {}

    def save_in_file(self):
        with open(self.filename, 'w') as fh:
            header_names = ['tag', 'create', 'note']
            writer = csv.DictWriter(fh, fieldnames = header_names, delimiter=',')
            writer.writeheader()
            for k, v in self.data.items():
                writer.writerow({'tag': k, 'create': v['create'], 'note': v['note']})   

class NotesCommands:

    def add_note(self, tag: str, note = "* empty note *"):
        create = datetime.now()
        if tag not in notesbook.data:   
            all_note_data = {"create": create.strftime("%d.%m.%Y %H:%M"), "note": note}
            notesbook.data[tag] = all_note_data
        else:
            return '**  a note with this name exists, if you want to change it enter the command: edit note  **'
        notesbook.save_in_file()
        return '** note added successfully **'

    def delete_note(self, tag: str):
        del notesbook.data[tag]
        notesbook.save_in_file()
        return f'** note {tag} delete successfully **'

    def edit_note(self, tag: str, note: str):
        notesbook.data[tag][tag] = note
        notesbook.save_in_file()
        return f'** note {tag} edit successfully **'
    
    def show_some_note(self, tag: str):
        result = f'''date create note: {notesbook.data[tag]["create"]}\nnote text: {notesbook.data[tag]["note"]}\n'''
        print(result)
        return result

    def show_all_notes(self):
        result = "\n*** ALL YOUR NOTES ***\n\n"
        for k, v in notesbook.data.items():
            result += f'''tag: {k}\ncreate: {v["create"]}\nnote: {v["note"]}\n\n'''
        print(result)
        return result

    def find_note(self, request: str):
        find = ""
        for k, v in notesbook.data.items():
            if request in k:
                find += f'''tag: {k}\ncreate: {v["create"]}\nnote: {v["note"]}\n\n'''
        if find == "":
            print('*** No notes were found matching your request ***')
        else:
            result = "\n*** FIND NEXT NOTES ***\n\n" + find
        print(result)
        return result
        
# *** next need deleted ***
# НАСТУПНИЙ КОД ТІЛЬКИ ДЛЯ ПЕРЕВІРКИ ОКРЕМОГО ФУНКЦІОНУВАННЯ РОБОТИ З НОТАТКАМИ (ВИДАЛИТИ ПРИ ІНТЕГРУВАННІ)

# mini handler only for test
notesbook = NotesBook()
notescommands = NotesCommands()
notesbook.read_file()
welcome = """\n*** start a mini CLI-bot (only for test notes) ***
 ДОСТУПНІ КОМАНДИ:
new note - команда додавання нового нотатка (після введення команди спочатку запросить назву нотатка, потім сам текст нотатка)
delete note - команда видалення нотатка
edit note - команта редагування нотатка
all notes - відобразити всі створені нотатки
note - команда відображення певного нотатка (після введення команди спочатку запросить назву нотатка, потім виведе текст нотатка)
find note - пошук нотатка по назві
stop - вихід з циклу Бота
"""
print(welcome)

while True:
    userinput = input(": ")
    if userinput.lstrip().lower() == "stop":
        print('*** mini CLI-bot end of work (only for test notes) ***\n')
        break
    elif userinput.lstrip().lower() == "new note":
        input_tag = input(": enter note name: ")
        input_note_text = input(": enter note text: ")
        notescommands.add_note(input_tag, input_note_text)
    elif userinput.lstrip()[0:11].lower() == "delete note":
        input_tag = input(": name of the note you want to delete: ")
        if input_tag not in notesbook.data:
            print(f': note with name: {input_tag} does not find')
        else:
            confirm = input(": do you really want to delete y/n: ")
            if confirm.lower() == "y":
                notescommands.delete_note(input_tag)
    elif userinput.lstrip()[0:9].lower() == "edit note":
        input_tag = input(": name of the note you want to edit: ")
        if input_tag not in notesbook.data:
            print(f': note with name: {input_tag} does not find')
        else:
            new_note = input(": enter new text for note: ")
            notescommands.edit_note(input_tag, new_note)
    elif userinput.lstrip().lower() == "all notes":
        notescommands.show_all_notes()
    elif userinput.lstrip().lower() == "note":
        input_tag = input(": enter the name of the note you want to view: ")
        if input_tag not in notesbook.data:
            print(f': note with name: {input_tag} does not find')
        else:
            notescommands.show_some_note(input_tag)
    elif userinput.lstrip().lower() == "find note":
        request = input(": enter a query to search: ")
        notescommands.find_note(request)       


# python3 notes.py

# залишилось зробити теги окремо ллістом з сортуванням і відображенням по тегам

# зберігати нотатки з текстовою інформацією;
# проводити пошук за нотатками;
# редагувати та видаляти нотатки;
# додавати в нотатки "теги", ключові слова, що описують тему та предмет запису;
# здійснювати пошук та сортування нотаток за ключовими словами (тегами);

# add_note(tag: str, note: str)
# delete_note(tag: str)
# edit_note(tag: str, note: str)





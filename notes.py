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

class NotesCommands(NotesBook):

    def add_note(self, tag: str, note: str, notesbook1: NotesBook) -> str:
        notesbook1.read_file()
        create = datetime.now()
        if tag not in notesbook1.data:   
            all_note_data = {"create": create.strftime("%d.%m.%Y %H:%M"), "note": note}
            notesbook1.data[tag] = all_note_data
            notesbook1.save_in_file()
            return '** note added successfully **'
        else:
            print(f'\033[33mnote with name \033[43m {input_tag} \033[0m\033[33m exists, if you want to change it enter the command: edit note\033[37m')


    def delete_note(self, tag: str, notesbook1: NotesBook):
        notesbook1.read_file()
        if input_tag not in notesbook1.data:
            print(f'\033[33mnote with name \033[43m {input_tag} \033[0m\033[33m does not find\033[0m')
        else:
            del notesbook1.data[tag]
            notesbook1.save_in_file()
            return f'** note {tag} delete successfully **'

    def edit_note(self, tag: str, note: str, notesbook1: NotesBook):
        notesbook1.read_file()
        if tag not in notesbook1.data:
            print(f'\033[33mnote with name \033[43m {tag} \033[0m\033[33m does not find\033[0m')
        else:
            notesbook1.data[tag]["note"] = note
            notesbook1.save_in_file()
            return f'** note {tag} edit successfully **'
    
    def show_some_note(self, tag: str,  notesbook1: NotesBook):
        notesbook1.read_file()
        if tag not in notesbook1.data:
            print(f'\033[33mnote with name \033[43m {tag} \033[0m\033[33m does not find\033[0m')
        else:
            result = f'''date create note: {notesbook1.data[tag]["create"]}\nnote text: {notesbook1.data[tag]["note"]}\n'''
            print(result)
            return result

    def show_all_notes(self, notesbook1: NotesBook):
        notesbook1.read_file()
        result = "\033[32m\n*** ALL YOUR NOTES ***\033[0m\n\n"
        for k, v in notesbook1.data.items():
            result += f'''tag: {k}\ncreate: {v["create"]}\nnote: {v["note"]}\n\n'''
        print(result)
        return result

    def find_note(self, request: str, notesbook1: NotesBook):
        notesbook1.read_file()
        find = ""
        for k, v in notesbook1.data.items():
            if request in k:
                find += f'''tag: {k}\ncreate: {v["create"]}\nnote: {v["note"]}\n\n'''
        if find == "":
            print('\033[33m*** No notes were found matching your request ***\033[0m')
        else:
            result = "\033[32m\n*** FIND NEXT NOTES ***\n\n\033[0m" + find
            print(result)
            return result
        
# *** next need deleted ***
# НАСТУПНИЙ КОД ТІЛЬКИ ДЛЯ ПЕРЕВІРКИ ОКРЕМОГО ФУНКЦІОНУВАННЯ РОБОТИ З НОТАТКАМИ (ВИДАЛИТИ ПРИ ІНТЕГРУВАННІ)
# mini handler only for test

notescommands = NotesCommands()

welcome = """ДОСТУПНІ КОМАНДИ:
new note - команда додавання нового нотатка (після введення команди спочатку запросить назву нотатка, потім сам текст нотатка)
delete note - команда видалення нотатка
edit note - команта редагування нотатка
all notes - відобразити всі створені нотатки
note - команда відображення певного нотатка (після введення команди спочатку запросить назву нотатка, потім виведе текст нотатка)
find note - пошук нотатка по назві
stop - вихід з циклу Бота
"""
print('\033[32m\n*** start a mini CLI-bot (only for test notes) ***\n\033[0m')
print(welcome)
while True:
    userinput = input(": ")
    if userinput.lstrip().lower() == "stop":
        print('\033[32m*** mini CLI-bot end of work (only for test notes) ***\n\033[0m')
        break
    elif userinput.lstrip().lower() == "new note":
        input_tag = input(": enter note name: ")
        input_note_text = input(": enter note text: ")
        notescommands.add_note(input_tag, input_note_text, NotesBook())
    elif userinput.lstrip()[0:11].lower() == "delete note":
        input_tag = input(": name of the note you want to delete: ")
        confirm = input(": do you really want to delete y/n: ")
        if confirm.lower() == "y":
            notescommands.delete_note(input_tag, NotesBook())
    elif userinput.lstrip()[0:9].lower() == "edit note":
        input_tag = input(": name of the note you want to edit: ")
        new_note = input(": enter new text for note: ")
        notescommands.edit_note(input_tag, new_note, NotesBook())
    elif (userinput.lstrip().lower() == "all notes") or (userinput.lstrip().lower() == "all note"):
        notescommands.show_all_notes(NotesBook())
    elif userinput.lstrip().lower() == "note":
        input_tag = input(": enter the name of the note you want to view: ")
        notescommands.show_some_note(input_tag, NotesBook())
    elif userinput.lstrip().lower() == "find note":
        request = input(": enter a query to search: ")
        notescommands.find_note(request, NotesBook())       


# python3 notes.py

# залишилось зробити теги окремо ллістом з сортуванням і відображенням по тегам
# init open read file when start
# зберігати нотатки з текстовою інформацією;
# проводити пошук за нотатками; - пошук зробити по всі полям крім тегів
# редагувати та видаляти нотатки;
# додавати в нотатки "теги", ключові слова, що описують тему та предмет запису;
# здійснювати пошук та сортування нотаток за ключовими словами (тегами);
# красивое форматирование отображения всех заметок
# add_note(tag: str, note: str)
# delete_note(tag: str)
# edit_note(tag: str, note: str)
# описати всі def

#   name:  love music
#   tags:  song, music
# create:  '10.09.2022 18:30'
#   note:  ac-dc beatles brainstorm avril lavine

# tag: newmusic 1
# create: 10.09.2022 19:26
# note: rty uio fgh nmj


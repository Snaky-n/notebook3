from src.config import Config
from src.storage import Storage
from src.note import Note
from src.search import Search


class Interface:
    def __init__(self, config_path: str):
        self.config = Config(config_path)
        self.storage = Storage(self.config.database_path)
        self.search = Search()
        self.note = Note("Заголовок заметки", "Содержимое заметки")

    def run(self):
        while True:
            print("Выберите действие:")
            print("1 - Показать все заметки")
            print("2 - Найти заметки")
            print("3 - Создать заметку")
            print("4 - Редактировать заметку")
            print("5 - Удалить заметку")
            print("0 - Выход")
            choice = input()
            if choice == '1':
                self.show_notes()
            elif choice == '2':
                self.search_notes()
            elif choice == '3':
                self.create_note()
            elif choice == '4':
                self.edit_note()
            elif choice == '5':
                self.delete_note()
            elif choice == '0':
                break
            else:
                print("Неправильный выбор")

    def show_notes(self):
        notes = self.storage.get_all_notes()
        if not notes:
            print("Заметок нет")
        else:
            for note in notes:
                print(note)

    def search_notes(self):
        query = input("Введите поисковый запрос: ")
        results = self.search.search_notes(query)
        if not results:
            print("Ничего не найдено")
        else:
            for result in results:
                print(result)

    def create_note(self):
        title = input("Введите заголовок заметки: ")
        content = input("Введите текст заметки: ")
        note = self.note.create(title, content)
        self.storage.add_note(note)

    def edit_note(self):
        note_id = input("Введите id заметки: ")
        note = self.storage.get_note_by_id(note_id)
        if not note:
            print("Заметка не найдена")
        else:
            title = input(f"Введите новый заголовок для заметки '{note.title}': ")
            content = input(f"Введите новый текст для заметки '{note.content}': ")
            updated_note = self.note.update(note, title, content)
            self.storage.update_note_by_id(note_id, updated_note)

    def delete_note(self):
        note_id = input("Введите id заметки: ")
        note = self.storage.get_note_by_id(note_id)
        if not note:
            print("Заметка не найдена")
        else:
            self.storage.delete_note_by_id(note_id)
            print(f"Заметка с id {note_id} удалена")

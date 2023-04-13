import datetime


class Note:
    """Класс для создания заметок"""

    def __init__(self, title, content, tags=None):
        """
        Создает новую заметку.

        title (str): заголовок заметки
        content (str): содержимое заметки
        tags (list[str]): список тегов для заметки
        """
        self.title = title
        self.content = content
        self.tags = tags or []
        self.creation_date = datetime.datetime.now()

    def __str__(self):
        """
        Возвращает строковое представление заметки в формате:
        <заголовок>
        <содержимое>
        <теги>
        <дата создания>
        """
        tags = ", ".join(self.tags)
        creation_date = self.creation_date.strftime("%d-%m-%Y %H:%M:%S")
        return f"{self.title}\n{self.content}\n{tags}\n{creation_date}"

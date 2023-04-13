
from typing import List
from src.note import Note


class Search:
    def __init__(self):
        pass

    @staticmethod
    def by_title(notes: List[Note], query: str) -> List[Note]:
        """
        Returns a list of notes whose title contains the query string
        """
        return [note for note in notes if query.lower() in note.title.lower()]

    @staticmethod
    def by_content(notes: List[Note], query: str) -> List[Note]:
        """
        Returns a list of notes whose content contains the query string
        """
        return [note for note in notes if query.lower() in note.content.lower()]

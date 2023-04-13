import sqlite3

from src.config import Config


class Database:
    def __init__(self, config: Config):
        self.connection = sqlite3.connect(config.database_file)
        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        # Create table for notes
        cursor.execute('''CREATE TABLE IF NOT EXISTS notes
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                         title TEXT NOT NULL,
                         content TEXT NOT NULL,
                         created_at TEXT NOT NULL,
                         updated_at TEXT NOT NULL)''')

        self.connection.commit()

    def get_all_notes(self):
        cursor = self.connection.cursor()

        # Get all notes from the database
        cursor.execute('''SELECT * FROM notes''')
        rows = cursor.fetchall()

        return rows

    def add_new_note(self, title, content, created_at, updated_at):
        cursor = self.connection.cursor()

        # Add a new note to the database
        cursor.execute('''INSERT INTO notes(title, content, created_at, updated_at)
                        VALUES(?,?,?,?)''', (title, content, created_at, updated_at))

        self.connection.commit()

    def update_note_by_id(self, note_id, title, content, updated_at):
        cursor = self.connection.cursor()

        # Update a note in the database by its ID
        cursor.execute('''UPDATE notes SET title=?, content=?, updated_at=?
                        WHERE id=?''', (title, content, updated_at, note_id))

        self.connection.commit()

    def delete_note_by_id(self, note_id):
        cursor = self.connection.cursor()

        # Delete a note from the database by its ID
        cursor.execute('''DELETE FROM notes WHERE id=?''', (note_id,))

        self.connection.commit()

    def get_note_by_id(self, note_id):
        cursor = self.connection.cursor()

        # Get a note from the database by its ID
        cursor.execute('''SELECT * FROM notes WHERE id=?''', (note_id,))
        row = cursor.fetchone()

        return row

    def __del__(self):
        self.connection.close()


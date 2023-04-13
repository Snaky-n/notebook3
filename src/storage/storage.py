import os


class Storage:
    def __init__(self, db_path):
        self.db_path = db_path

    def save(self, data):
        with open(self.db_path, 'a') as f:
            f.write(data + os.linesep)

    def load(self):
        if not os.path.exists(self.db_path):
            return []
        with open(self.db_path, 'r') as f:
            return [line.strip() for line in f.readlines()]

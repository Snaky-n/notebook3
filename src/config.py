import os
import json

class Config:
    """Класс для работы с конфигурационным файлом"""

    def __init__(self, config_path):
        self.config_path = config_path
        self.database_path = ""
        self.attachments_path = ""

    def load(self):
        with open(self.config_path, "r") as f:
            data = json.load(f)

        self.database_path = data["database"]["name"]
        self.attachments_path = f"{self.database_path}_attachments"


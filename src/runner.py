from abc import ABC, abstractmethod
import json
import os


from src.utils.logger import Logger


class Runner(ABC):
    def __init__(self, client):
        self.client = client
        self.logger = Logger()

    @abstractmethod
    def run(self):
        pass

    def load_file(self, filename):
        with open(filename, "r") as file:
            return json.load(file)

    def write_to_json_file(self, filepath, file_content):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            file.write(json.dumps(file_content, indent=2))

    def write_to_file(self, filepath, file_content):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as file:
            file.write(file_content)

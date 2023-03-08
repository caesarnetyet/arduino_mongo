import json


class ParseJson:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except:
            self.write([])
            return []

    def write(self, data):
        with open(self.file_path, 'w+') as f:
            json.dump(data, f)

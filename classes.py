import json

class Deploy():

    def __init__(self, file):
        self.payload = self.parse_json(file)

    def parse_json(self, file):
        return(json.load(file))

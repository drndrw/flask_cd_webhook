import json

class Deploy():

    def __init__(self, file):
        # self.payload = self.parse_json(file)
        self.test = "test"

    def parse_json(self, file):
        return(json.loads(file))

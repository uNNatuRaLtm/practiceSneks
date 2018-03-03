from brain import decide
from base_snake import BaseSnake
import json

class Snake3(BaseSnake):

    def move(self, data):
        decision = decide(data)
        return decision

    def name(self):
        return "Training Snake 3"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self,data):
        with open(self.name()+'.txt', 'a') as file:
            file.write(json.dumps(data))
        pass

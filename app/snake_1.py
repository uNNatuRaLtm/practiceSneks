from brain import decide
from snake_0 import Snake0
import json

class Snake1(Snake0):

    def move(self, data):
        decision = decide(data)
        return decision

    def name(self):
        return "Training Snake 1"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self, data):
        with open(self.name()+'.txt', 'a') as file:
            file.write(json.dumps(data))
        pass

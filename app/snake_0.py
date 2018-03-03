from base_snake import BaseSnake
from brain import decide
import json
class Snake0(BaseSnake):

    def move(self, data):
        decision = decide(data)
        return decision

    def name(self):
        return "Training Snake 0"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self,data):
        pass

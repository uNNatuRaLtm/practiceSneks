from brain import decide
from base_snake import BaseSnake


class Snake2(BaseSnake):

    def move(self, data):
        decision = decide(data)
        return decision

    def name(self):
        return "Training Snake 2"

    def color(self):
        return "#05f299"

    def head_url(self):
        return ""

    def taunt(self):
        return ""

    def end(self):
        pass

class BaseSnake(object):

    def move(self, data):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def name(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def color(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def head_url(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def taunt(self):
        raise NotImplemented("this should be overridden on implementations of snakes")

    def end(self,data):
        raise NotImplemented("this should be overridden on implementations of snakes")

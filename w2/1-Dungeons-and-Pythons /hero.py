from entity import Entity

class Hero(Entity):
    def __init__(self, name, health, nick_name):
        super().__init__(name, health)
        self.nick_name = nick_name


    def known_as(self):
        str_result = super().known_as() + " the " + self.nick_name
        return str_result

 
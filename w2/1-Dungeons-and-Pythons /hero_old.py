class Hero():
    def __init__(self, name, health, nick_name):
        self.name = name
        self._MAX_HEALT= health
        self.nick_name = nick_name
        self.health = health

    def known_as(self):
        str_result = self.name + " the " + self.nick_name
        return str_result

    def  is_alive(self):
        alive = self.health > 0
        return alive

    def get_health(self):
        return self.health


    def take_damage(self, damage_points):
        if damage_points >= self.health:
            self.health = 0

        else:
            self.health = self.health - damage_points

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        else:
            self.health = self.health + healing_points
            if self.health > self._MAX_HEALT:
                self.health = self._MAX_HEALT

            return True

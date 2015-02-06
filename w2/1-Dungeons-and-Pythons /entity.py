from weapon import Weapon
class Entity():
    def __init__(self, name, health):
        self.name = name
        self._MAX_HEALT= health
        self.health = health
        self.weapon = 0

    def known_as(self):
        str_result = self.name
        return str_result

    def is_alive(self):
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

    def has_weapon(self):
        return type(self.weapon) is Weapon

    def equip_weapon(self, weapon):
        self.weapon = weapon


    def attack(self):
        if not self.has_weapon():
            return 0
        if self.weapon.critical_hit():
            return self.weapon.damage * 2
        else:
            return self.weapon.damage
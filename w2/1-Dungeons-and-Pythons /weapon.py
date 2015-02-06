from random import random
class Weapon():
    def __init__(self, name, damage, critical_strike_percent):
        self. name = name
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent
        self._RAW_DAMAGE = damage
        
    def critical_hit(self):
        if random() <= self.critical_strike_percent:
            return True
        else:
            return False
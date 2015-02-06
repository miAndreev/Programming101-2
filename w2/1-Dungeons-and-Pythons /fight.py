from hero import Hero 
from orc import Orc
from random import randint

class Fight():
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def get_order(self):
        if randint(0,100) < 50:
            return (self.defender, self.attacker)
        else:
            return(self.attacker, self.defender)

    def simulate_fight(self):
        attacker, defender = self.get_order()

        while self.attacker.is_alive() and self.defender.is_alive():
            damage = attacker.attack()
            defender.take_damage(damage)

            attacker, defender = defender, attacker

from hero import Hero 
from orc import Orc
from weapon import Weapon
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero("Bron", 100, "DragonSlayer")
        self.test_ork = Orc("Vilasteros", 100, 1.34)
        self.bow = Weapon("Mighty Bow", 13, 0.17)
        self.axe = Weapon("Thunder Axe", 19, 0.25)
        self.test_ork.equip_weapon(self.bow)
        self.test_hero.equip_weapon(self.axe)
        self.battle = Fight(self.test_hero, self.test_ork)

    def test_init(self):
        self.assertEqual(self.battle.attaker, self.test_hero)
        self.assertEqual(self.battle.orc, self.test_ork)

    def test_simulate_fight(self):
        self.battle.simulate_fight()
        self.assertTrue(self.test_hero.is_alive() ^ self.test_ork.is_alive())

    def test_fight_with_no_weapons_orc(self):
        self.test_ork.equipped_weapon = None
        self.battle.simulate_fight()
        self.assertTrue(self.test_hero.is_alive())

    def test_fight_with_no_weapons_hero(self):
        self.test_hero.equipped_weapon = None
        self.battle.simulate_fight()
        self.assertTrue(self.test_ork.is_alive())


if __name__ == '__main__':
    unittest.main()
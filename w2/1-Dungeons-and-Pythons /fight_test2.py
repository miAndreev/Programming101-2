from hero import Hero 
from orc import Orc
from weapon import Weapon
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero("Bron", 100, "DragonSlayer") 
        self.test_orc = Orc("Bron", 100, 1.25)
        self.test_orc.equip_weapon(Weapon("Mighty Bow", 13, 0.17))
        self.test_hero.equip_weapon(Weapon("Mighty Bow", 13, 0.17))



if __name__ == '__main__':
    unittest.main()
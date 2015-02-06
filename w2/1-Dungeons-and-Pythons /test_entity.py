from entity import Entity
from weapon import Weapon
import unittest

class MyTests(unittest.TestCase):
    def setUp(self):
        self.test_ent = Entity("Bron", 100)
        self.weap = Weapon("Mighty Bow", 13, 0.17)

    def test_init(self): 
        self.assertEqual(self.test_ent.name, "Bron")
        self.assertEqual(self.test_ent.health, 100)
        self.assertEqual(self.test_ent._MAX_HEALT, 100)

    def test_known_as(self):
        self.assertEqual(self.test_ent.known_as(), "Bron")

    def test_is_alive(self):
        self.assertEqual(self.test_ent.is_alive(), True)

    def test_get_health(self):
        self.assertEqual(self.test_ent.get_health(), 100)

    def test_take_damage(self):
        self.test_ent.take_damage(50)
        self.assertEqual(self.test_ent.health, 50)
        self.test_ent.take_damage(60)
        self.assertEqual(self.test_ent.health, 0)
    
    def test_take_healing(self):
        self.test_ent.health = 50
        self.assertTrue(self.test_ent.take_healing(20))
        self.assertEqual(self.test_ent.health, 70)
    
    def test_take_healing_above_max(self):
        self.test_ent.health = 20
        self.test_ent.take_healing(120)
        self.assertEqual(self.test_ent.health, 100)
    
    def test_healing_on_dead(self):
        self.test_ent.health = 0
        self.assertFalse(self.test_ent.take_healing(100))

    def test_have_no_w(self):
        self.assertEqual(self.test_ent.has_weapon(), False)

    def test_have_w(self):
        self.test_ent.equip_weapon(self.weap)
        self.assertEqual(self.test_ent.has_weapon(), True)

    def test_attack_no_weapon(self):
        self.assertEqual(self.test_ent.attack(), 0)

    def test_attack_weapon(self):
        self.test_ent.equip_weapon(self.weap)
        self.assertEqual(self.test_ent.attack(), 13)



if __name__ == '__main__':
    unittest.main()
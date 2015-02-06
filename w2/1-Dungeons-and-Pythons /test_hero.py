from hero import Hero
import unittest

class MyTests(unittest.TestCase):
    def setUp(self):
        self.test_hero = Hero("Bron", 100, "DragonSlayer")

    def test_init(self): 
        self.assertEqual(self.test_hero.name, "Bron")
        self.assertEqual(self.test_hero.health, 100)
        self.assertEqual(self.test_hero._MAX_HEALT, 100)
        self.assertEqual(self.test_hero.nick_name, "DragonSlayer")

    def test_known_as(self):
        self.assertEqual(self.test_hero.known_as(), "Bron the DragonSlayer")

    def test_is_alive(self):
        self.assertEqual(self.test_hero.is_alive(), True)

    def test_get_health(self):
        self.assertEquals(self.test_hero.get_health(), 100)

    def test_take_damage(self):
        self.test_hero.take_damage(50)
        self.assertEqual(self.test_hero.health, 50)
        self.test_hero.take_damage(60)
        self.assertEqual(self.test_hero.health, 0)
    
    def test_take_healing(self):
        self.test_hero.health = 50
        self.assertTrue(self.test_hero.take_healing(20))
        self.assertEqual(self.test_hero.health, 70)
    
    def test_take_healing_above_max(self):
        self.test_hero.health = 20
        self.test_hero.take_healing(120)
        self.assertEqual(self.test_hero.health, 100)
    
    def test_healing_on_dead(self):
        self.test_hero.health = 0
        self.assertFalse(self.test_hero.take_healing(100))


if __name__ == '__main__':
    unittest.main()
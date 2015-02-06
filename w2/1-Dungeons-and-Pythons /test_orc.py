from orc import Orc
import unittest

class MyTests(unittest.TestCase):
    def setUp(self):
        self.test_orc = Orc("Bron", 100, 1.25)

    def test_init(self): 
        self.assertEqual(self.test_orc.name, "Bron")
        self.assertEqual(self.test_orc.health, 100)
        self.assertEqual(self.test_orc._MAX_HEALT, 100)
        self.assertEqual(self.test_orc.berserk_factor, 1.25)

    def test_known_as(self):
        self.assertEqual(self.test_orc.known_as(), "Bron")

    def test_is_alive(self):
        self.assertEqual(self.test_orc.is_alive(), True)



    def test_get_health(self):
        self.assertEquals(self.test_orc.get_health(), 100)

    def test_take_damage(self):
        self.test_orc.take_damage(50)
        self.assertEqual(self.test_orc.health, 50)
        self.test_orc.take_damage(60)
        self.assertEqual(self.test_orc.health, 0)
    
    def test_take_healing(self):
        self.test_orc.health = 50
        self.assertTrue(self.test_orc.take_healing(20))
        self.assertEqual(self.test_orc.health, 70)
    
    def test_take_healing_above_max(self):
        self.test_orc.health = 20
        self.test_orc.take_healing(120)
        self.assertEqual(self.test_orc.health, 100)
    
    def test_healing_on_dead(self):
        self.test_orc.health = 0
        self.assertFalse(self.test_orc.take_healing(100))


if __name__ == '__main__':
    unittest.main()
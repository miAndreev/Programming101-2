import unittest
from weapon import Weapon

class Tests(unittest.TestCase):
    def setUp(self):
        self.bow = Weapon("Mighty Bow", 13, 0.17)

    def test_init(self):
        self.assertEqual(self.bow.name, "Mighty Bow")
        self.assertEqual(self.bow.damage, 13)
        self.assertEqual(self.bow.critical_strike_percent, 0.17)
        
    def test_if_critical_hit(self):
        crits = []
        for i in range(100):
            crits.append(self.bow.critical_hit())
        self.assertTrue(True in crits)

if __name__ == '__main__':
    unittest.main()
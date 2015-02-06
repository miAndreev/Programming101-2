from solution import calculate_coins
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(calculate_coins(0.53), {1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0})

    def test_two(self):
        self.assertEquals(calculate_coins(8.94), {1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2})



if __name__ == '__main__':
    unittest.main()
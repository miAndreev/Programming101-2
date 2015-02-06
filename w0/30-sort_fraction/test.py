from solution import sort_fractions
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(sort_fractions([(2, 3), (1, 2)]), [(1, 2), (2, 3)])
    def test_two(self):
        self.assertEquals(sort_fractions([(2, 3), (1, 2), (1, 3)]), [(1, 3), (1, 2), (2, 3)])
    def test_three(self):
        self.assertEquals(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]), [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)])



if __name__ == '__main__':
    unittest.main()
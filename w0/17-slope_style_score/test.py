from solution import slope_style_score
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(94.66, slope_style_score([94, 95, 95, 95, 90]))
    def test_two(self):
        self.assertEquals(80.0, slope_style_score([60, 70, 80, 90, 100]))
    def test_tree(self):
        self.assertEquals(93.5, slope_style_score([96, 95.5, 93, 89, 92]))


if __name__ == '__main__':
    unittest.main()
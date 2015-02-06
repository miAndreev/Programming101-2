from solution import contains_digit
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(False, contains_digit(123, 4))

    def test_two(self):
        self.assertEquals(True, contains_digit(42, 2))

    def test_vore(self):
        self.assertEquals(True, contains_digit(1000, 0))

    def test_five(self):
        self.assertEquals(False, contains_digit(12346789, 5))




if __name__ == '__main__':
    unittest.main()
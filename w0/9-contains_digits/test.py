from solution import contains_digits
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(True, contains_digits(402123, [0, 3, 4]))

    def test_two(self):
        self.assertEquals(False, contains_digits(666, [6,4]))

    def test_tree(self):
        self.assertEquals(False, contains_digits(123456789, [1,2,3,0]))

    def test_vore(self):
        self.assertEquals(True, contains_digits(456, []))



if __name__ == '__main__':
    unittest.main()
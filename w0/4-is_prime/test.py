from solution import is_prime
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(False, is_prime(1))

    def test_two(self):
        self.assertEquals(True, is_prime(2))

    def test_tree(self):
        self.assertEquals(False, is_prime(8))

    def test_four(self):
        self.assertEquals(True, is_prime(11))

    def test_five(self):
        self.assertEquals(False, is_prime(-10))


if __name__ == '__main__':
    unittest.main()
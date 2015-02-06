from solution import sum_of_divisors
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(15, sum_of_divisors(8))

    def test_two(self):
        self.assertEquals(8, sum_of_divisors(7))    

    def test_tree(self):
        self.assertEquals(1, sum_of_divisors(1))

    def test_vour(self):
        self.assertEquals(2340, sum_of_divisors(1000))


if __name__ == '__main__':
    unittest.main()
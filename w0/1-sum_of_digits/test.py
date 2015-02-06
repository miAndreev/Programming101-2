from solution import sum_of_digits
import unittest

class  MyTestCases(unittest.TestCase):
    def test_one(self):
        self.assertEqual(43, sum_of_digits(1325132435356))

    def test_two(self):
        self.assertEqual(6,sum_of_digits(123))

    def test_tree(self):
        self.assertEqual(6, sum_of_digits(6))

    def test_four(self):
        self.assertEqual(1, sum_of_digits(-10))

if __name__ == '__main__':
    unittest.main()
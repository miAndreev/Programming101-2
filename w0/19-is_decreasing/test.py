from solution import is_decreasing
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(True, is_decreasing([5,4,3,2,1]))

    def test_two(self):
        self.assertEquals(False, is_decreasing([1,2,3]))

    def test_three(self):
        self.assertEquals(True, is_decreasing([100, 50, 20]))

    def test_four(self):
        self.assertEquals(False, is_decreasing([1,1,1,1]))



if __name__ == '__main__':
    unittest.main()
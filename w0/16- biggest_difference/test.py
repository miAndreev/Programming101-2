from solution import biggest_difference
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(-1, biggest_difference([1,2]))

    def test_two(self):
        self.assertEquals(-4, biggest_difference([1,2,3,4,5]))

    def test_three(self):
        self.assertEquals(-9, biggest_difference([-10, -9, -1]))

    def test_vore(self):
        self.assertEquals(-99, biggest_difference(range(100)))



if __name__ == '__main__':
    unittest.main()
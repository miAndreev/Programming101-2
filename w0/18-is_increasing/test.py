from solution import is_increasing
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(True, is_increasing([1,2,3,4,5]))

    def test_two(self):
        self.assertEquals(True, is_increasing([1]))

    def test_three(self):
        self.assertEquals(False, is_increasing([5,6,-10]))

    def test_four(self):
        self.assertEquals(False, is_increasing([1,1,1,1]))



if __name__ == '__main__':
    unittest.main()
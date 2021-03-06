from solution import magic_square
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(magic_square([[1,2,3], [4,5,6], [7,8,9]]), False)
    def test_two(self):
        self.assertEquals(magic_square([[4,9,2], [3,5,7], [8,1,6]]), True)
    def test_three(self):
        self.assertEquals(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]), True)
    def test_foure(self):
        self.assertEquals(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]), True)
    def test_five(self):
        self.assertEquals(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]), False)

if __name__ == '__main__':
    unittest.main()
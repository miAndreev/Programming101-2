from solution import simplify_fraction  
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(simplify_fraction((3,9)), (1,3))
    def test_two(self):
        self.assertEquals(simplify_fraction((1,7)), (1,7))
    def test_three(self):
        self.assertEquals(simplify_fraction((4,10)), (2,5))



if __name__ == '__main__':
    unittest.main()
from solution import list_to_number
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(123, list_to_number([1,2,3]))

    def test_two(self):
        self.assertEquals(99999, list_to_number([9,9,9,9,9]))

    def test_tree(self):
        self.assertEquals(123023, list_to_number([1,2,3,0,2,3]))



if __name__ == '__main__':
    unittest.main()
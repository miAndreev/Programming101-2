from solution import number_to_list
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals([1,2,3], number_to_list(123))

    def test_two(self):
        self.assertEquals([9,9,9,9,9], number_to_list(99999))

    def test_tree(self):
        self.assertEquals([1,2,3,0,2,3], number_to_list(123023))



if __name__ == '__main__':
    unittest.main()
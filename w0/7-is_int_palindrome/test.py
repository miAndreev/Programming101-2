from solution import is_int_palindrome
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(True,is_int_palindrome(1))
    
    def test_two(self):
        self.assertEquals(False,is_int_palindrome(42))

    def test_tree(self):
        self.assertEquals(True,is_int_palindrome(100001))

    def test_vor(self):
        self.assertEquals(True,is_int_palindrome(999))

    def test_five(self):
        self.assertEquals(False,is_int_palindrome(123))


if __name__ == '__main__':
    unittest.main()
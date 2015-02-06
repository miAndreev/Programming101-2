from solution import is_an_bn
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(is_an_bn(""), True)
    def test_two(self):
        self.assertEquals(is_an_bn("rado"), False)
    def test_three(self):
        self.assertEquals(is_an_bn("aaabb"), False)
    def test_four(self):
        self.assertEquals(is_an_bn("aaabbb"), True)
    def test_five(self):
        self.assertEquals(is_an_bn("aabbaabb"), False)
    def test_six(self):
        self.assertEquals(is_an_bn("bbbaaa"), False)
    def test_seven(self):
        self.assertEquals(is_an_bn("aaaaabbbbb"), True)


if __name__ == '__main__':
    unittest.main()
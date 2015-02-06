from solution import count_consonants
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(4, count_consonants("Python"))

    def test_two(self):
        self.assertEquals(11, count_consonants("Theistareykjarbunga"))

    def test_tree(self):
        self.assertEquals(7, count_consonants("grrrrgh!"))

    def test_vour(self):
        self.assertEquals(44, count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_five(self):
        self.assertEquals(6, count_consonants("A nice day to code!"))



if __name__ == '__main__':
    unittest.main()
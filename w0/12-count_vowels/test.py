from solution import count_vowels
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(2, count_vowels("Python"))

    def test_two(self):
        self.assertEquals(8, count_vowels("Theistareykjarbunga"))

    def test_tree(self):
        self.assertEquals(0, count_vowels("grrrrgh!"))

    def test_vour(self):
        self.assertEquals(22, count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))

    def test_five(self):
        self.assertEquals(8, count_vowels("A nice day to code!"))



if __name__ == '__main__':
    unittest.main()
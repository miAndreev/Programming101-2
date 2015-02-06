from solution import unique_words_count
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(unique_words_count(["apple", "banana", "apple", "pie"]), 3)

    def test_two(self):
        self.assertEquals(unique_words_count(["python", "python", "python", "ruby"]), 2)

    def test_three(self):
        self.assertEquals(unique_words_count(["HELLO!"] * 10), 1)


if __name__ == '__main__':
    unittest.main()
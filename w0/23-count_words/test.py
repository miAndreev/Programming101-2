from solution import count_words
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(count_words(["apple", "banana", "apple", "pie"]), {'apple': 2, 'pie': 1, 'banana': 1})

    def test_two(self):
        self.assertEquals(count_words(["python", "python", "python", "ruby"]), {'ruby': 1, 'python': 3})




if __name__ == '__main__':
    unittest.main()
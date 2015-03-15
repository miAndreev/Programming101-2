import sys
import unittest
# sys.path.append("..")

import start


class StartTests(unittest.TestCase):
    def setUp(self):
        pass

    def testPassShort(self): 
        self.assertFalse(start.check_pass("a!A1", "b"))

    def test_pass_only_digits(self):
        self.assertFalse(start.check_pass("11111111111", "b"))

    def test_pass_digit_uppercase(self):
        self.assertFalse(start.check_pass("1aaa111aZ", "b"))

    def test_username_in_pass(self):
        self.assertFalse(start.check_pass("abc!3Ksdfd", "abc"))

    def test_pass_good(self):
        self.assertTrue(start.check_pass("1aZ@asa!ga", "vvv"))



if __name__ == '__main__':
    unittest.main()
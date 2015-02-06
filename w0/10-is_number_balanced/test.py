from solution import is_number_balanced
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(True, is_number_balanced(9))

    def test_two(self):
        self.assertEquals(True, is_number_balanced(11))

    def test_thee(self):
        self.assertEquals(False, is_number_balanced(13))

    def test_vour(self):
        self.assertEquals(True, is_number_balanced(121))

    def test_five(self):
        self.assertEquals(True, is_number_balanced(4518))

    def test_six(self):
        self.assertEquals(False, is_number_balanced(28471))

    def test_seven(self):
        self.assertEquals(True, is_number_balanced(1238033))



if __name__ == '__main__':
    unittest.main()
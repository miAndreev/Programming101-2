from solution import reduce_file_path
import unittest

class MyTests(unittest.TestCase):
    def test_one(self):
        self.assertEquals(reduce_file_path("/"), "/")
    def test_two(self):
        self.assertEquals(reduce_file_path("/srv/../"), "/")
    def test_three(self):
        self.assertEquals(reduce_file_path("/srv/www/htdocs/wtf/"), "/srv/www/htdocs/wtf")
    def test_foure(self):
        self.assertEquals(reduce_file_path("/srv/www/htdocs/wtf"), "/srv/www/htdocs/wtf")
    def test_five(self):
        self.assertEquals(reduce_file_path("/srv/./././././"), "/srv")
    def test_six(self):
        self.assertEquals(reduce_file_path("/etc//wtf/"), "/etc/wtf")
    def test_seven(self):
        self.assertEquals(reduce_file_path("/etc/../etc/../etc/../"), "/")
    def test_eigth(self):
        self.assertEquals(reduce_file_path("//////////////"), "/")
    def test_nine(self):
        self.assertEquals(reduce_file_path("/../"), "/")

if __name__ == '__main__':
    unittest.main()
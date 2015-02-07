import unittest
from team_maker import Team_Maker

class MyTests(unittest.TestCase):
    def setUp(self):
        self.teamMaker = Team_Maker()
        self.teamMaker.get_json_from_file("1.txt")
        
    def test_list(self):
    	self.assertEqual(self.teamMaker.list_all_courses(), 
    		['Core Java', 'System C', 'Frontend JavaScript', 'Programming 101  v2',
    		 'Android', 'NodeJS', 'Core Ruby', 'Angular JS'])

    def test_match_teams(self):
    	self.teamMaker.list_all_courses()
    	self.assertEqual(len(self.teamMaker.match_teams(0, 2, 1)), 8)

if __name__ == '__main__':
    unittest.main()

        

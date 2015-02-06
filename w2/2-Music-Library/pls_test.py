from song import Song
from playlist import Playlist
import unittest

class MyTests(unittest.TestCase):

    def setUp(self):
        self.test_song = Song("Tri momi", "Vievska grupa", "none", 0, 180, 320)
        self.test_pls = Playlist("test")
        self.song_mariiko = Song("mari mariiko", "oratnica", "none", 0, 200, 320)

    def test_pls_add_song(self):
        self.test_pls.add_song(self.test_song)
        self.assertTrue(self.test_song in self.test_pls.songs)
        self.test_pls.add_song(self.song_mariiko)
        self.assertTrue(self.song_mariiko in self.test_pls.songs)

    def test_pls_remove_song(self):
        self.test_pls.add_song(self.test_song)
        self.assertTrue(self.test_song in self.test_pls.songs)
        self.test_pls.remove_song(self.test_song.title)
        self.assertFalse(self.test_song in self.test_pls.songs)

    def test_pls_total_leng_one(self):

        self.test_pls.add_song(self.test_song)
        self.assertEqual(180, self.test_pls.total_length())

    def test_pls_total_leng_more(self):
        self.test_pls.add_song(self.test_song)
        self.test_pls.add_song(self.song_mariiko)
        self.assertEqual(380, self.test_pls.total_length())

    def test_removeing_disrated(self):
        self.test_pls.add_song(self.test_song)
        self.test_pls.add_song(self.song_mariiko)
        self.test_pls.remove_disrated(2)
        self.assertTrue(self.test_song not in self.test_pls.songs)
        
    def test_remove_bad_quality(self):
        self.test_song.bitrate = 64
        self.test_pls.add_song(self.test_song)
        self.test_pls.remove_bad_quality()
        self.assertTrue(self.test_song not in self.test_pls.songs)

    def test_show_artists(self):
        self.test_pls.add_song(self.test_song)
        self.test_pls.add_song(self.song_mariiko)
        self.assertEqual(self.test_pls.show_artists(), ['Vievska grupa', 'oratnica'])

    def test_str(self):
        self.test_pls.add_song(self.test_song)
        self.test_pls.add_song(self.song_mariiko)
        result_str = """Vievska grupa Tri momi - 3:00\noratnica mari mariiko - 3:20\n"""
        r_t = "Vievska grupa Tri momi - 3:00"
        r_m = "oratnica mari mariiko - 3:20"
        self.assertEqual(str(self.test_song), r_t)
        self.assertEqual(str(self.song_mariiko), r_m)
        self.assertEqual(str(self.test_pls), result_str)

if __name__ == '__main__':
    unittest.main()
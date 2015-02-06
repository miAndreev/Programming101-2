from song import Song
from playlist import Playlist
import unittest

class MyTests(unittest.TestCase):
    def setUp(self):
        self.test_song = Song("Tri momi", "Vievska grupa", "none", 0, 150, 320)

    def test_song_init(self):
        self.assertEqual(self.test_song.title, "Tri momi")
        self.assertEqual(self.test_song.artist, "Vievska grupa")
        self.assertEqual(self.test_song.album, "none")
        self.assertEqual(self.test_song.rating, 0)
        self.assertEqual(self.test_song.length, 150)
        self.assertEqual(self.test_song.bitrate, 320)
    
    def test_song_rating(self):
        self.test_song.rate(5)
        self.assertEqual(self.test_song.rating, 5)

    def test_str(self):
        self.assertEqual(str(self.test_song), 'Vievska grupa Tri momi - 2:30')


if __name__ == '__main__':
    unittest.main()
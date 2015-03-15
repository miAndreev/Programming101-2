import unittest
import sqlite3
import os
from os import path, remove
from magic_spells import Spells
from cinema import Cinema

class MyTests(unittest.TestCase):
	def setUp(self):
		self.cinema = Cinema("test1.db")

	def test_a(self):
		self.cinema = Cinema("test1.db")

		self.cinema.add_movie('The Hunger Games: Catching Fire', 7.9)
		self.cinema.add_movie('Wreck-It Ralph', 7.8)
		self.cinema.add_movie('Her', 8.3)

		self.cinema.add_projection(1, '3D',  '2014-04-01', '19:10')
		self.cinema.add_projection(1, '2D',  '2014-04-01', '19:00')
		self.cinema.add_projection(1, '4DX', '2014-04-02', '21:00')
		self.cinema.add_projection(3, '2D',  '2014-04-05', '20:20')
		self.cinema.add_projection(2, '3D',  '2014-04-02', '22:00')
		self.cinema.add_projection(2, '2D',  '2014-04-02', '19:30')

		self.cinema.add_reservation('RadoRado', 1, 2, 1)
		self.cinema.add_reservation('RadoRado', 1, 3, 5)
		self.cinema.add_reservation('RadoRado', 1, 7, 8)
		self.cinema.add_reservation('Ivo', 3, 1, 1)
		self.cinema.add_reservation('Ivo', 3, 1, 2)
		self.cinema.add_reservation('Mysterious', 5, 2, 3)
		self.cinema.add_reservation('Mysterious', 5, 2, 4)

	def test_fetch_movie(self):
		movie = self.cinema.fetch_movie(3)
		self.assertEqual(movie[0], "Her")
		self.assertEqual(movie[1], 8.3)

	def test_fetch_fetch_movies(self):
		movies = self.cinema.fetch_movies()
		self.assertTrue((1, 'The Hunger Games: Catching Fire', 7.9) in movies)
		self.assertTrue((2, 'Wreck-It Ralph', 7.8) in movies)
		self.assertTrue((3, 'Her', 8.3) in movies)

	def test_fetch_projections_by_id(self):
		proj = self.cinema.fetch_projections_by_id(2)
		self.assertTrue((6, '2014-04-02', '19:30', '2D') in proj)
		self.assertTrue((5, '2014-04-02', '22:00', '3D') in proj)

	def test_fetch_projections_by_id_and_date(self):
		proj = self.cinema.fetch_projections_by_id_and_date(1, '2014-04-01')
		self.assertTrue((2, '19:00', '2D') in proj)
		self.assertTrue((1, '19:10', '3D') in proj)

	def test_fetch_taken_seats(self):
		taken = self.cinema.fetch_taken_seats(4)
		self.assertEqual(taken, [])
		taken = self.cinema.fetch_taken_seats(5)
		self.assertTrue((2, 3) in taken)
		self.assertTrue((2, 4) in taken)

	def test_free_place_for_projection(self):
		testing_value = self.cinema.free_place_for_projection(1)
		self.assertEqual(testing_value, 97)
		testing_value = self.cinema.free_place_for_projection(2)
		self.assertEqual(testing_value, 100)

	def test_fetch_projection(self):
		proj = self.cinema.fetch_projection(2)
		self.assertEqual(proj[0], ('2014-04-01', '19:00', '2D'))


	def test_z(self):
		os.remove("test1.db")


if __name__ == '__main__':
    unittest.main()
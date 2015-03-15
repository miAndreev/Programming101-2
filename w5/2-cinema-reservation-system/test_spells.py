import unittest
import sqlite3
import os
from os import path, remove
from magic_spells import Spells
from cinema import Cinema

class MyTests(unittest.TestCase):
	def setUp(self):
		self.spells = Spells("test1.db")
		
	def test_a(self):
		self.spells.cinema.add_movie('The Hunger Games: Catching Fire', 7.9)
		self.spells.cinema.add_movie('Wreck-It Ralph', 7.8)
		self.spells.cinema.add_movie('Her', 8.3)

		self.spells.cinema.add_projection(1, '3D',  '2014-04-01', '19:10')
		self.spells.cinema.add_projection(1, '2D',  '2014-04-01', '19:00')
		self.spells.cinema.add_projection(1, '4DX', '2014-04-02', '21:00')
		self.spells.cinema.add_projection(3, '2D',  '2014-04-05', '20:20')
		self.spells.cinema.add_projection(2, '3D',  '2014-04-02', '22:00')
		self.spells.cinema.add_projection(2, '2D',  '2014-04-02', '19:30')

		self.spells.cinema.add_reservation('RadoRado', 1, 2, 1)
		self.spells.cinema.add_reservation('RadoRado', 1, 3, 5)
		self.spells.cinema.add_reservation('RadoRado', 1, 7, 8)
		self.spells.cinema.add_reservation('Ivo', 3, 1, 1)
		self.spells.cinema.add_reservation('Ivo', 3, 1, 2)
		self.spells.cinema.add_reservation('Mysterious', 5, 2, 3)
		self.spells.cinema.add_reservation('Mysterious', 5, 2, 4)

	def test_show_movie(self):
		movie = self.spells.show_movie(3)
		self.assertEqual("Her (8.300000)", movie)

	def test_show_movies(self):
		movies = self.spells.show_movies()
		self.assertTrue('[1] - The Hunger Games: Catching Fire (7.900000)' in movies)
		self.assertTrue('[2] - Wreck-It Ralph (7.800000)' in movies)
		self.assertTrue('[3] - Her (8.300000)' in movies)

	def test_show_pojections_by_id(self):
		proj = self.spells.show_pojections_by_id(1)
		self.assertTrue('[2] - 2014-04-01 19:00 (2D)' in proj)
		self.assertTrue('[1] - 2014-04-01 19:10 (3D)' in proj)
		self.assertTrue('[3] - 2014-04-02 21:00 (4DX)' in proj)

	def test_show_pojections_by_id_and_date(self):
		proj = self.spells.show_pojections_by_id_and_date(1, "2014-04-01")
		self.assertTrue("[2] - 19:00 (2D)" in proj)
		self.assertTrue('[1] - 19:10 (3D)' in proj)

	def test_show_movie_projections(self):
		proj = self.spells.show_movie_projections(["a",1])
		self.assertTrue('[2] - 2014-04-01 19:00 (2D)' in proj)
		self.assertTrue('[1] - 2014-04-01 19:10 (3D)' in proj)
		self.assertTrue('[3] - 2014-04-02 21:00 (4DX)' in proj)

		proj = self.spells.show_movie_projections(["a", 1, "2014-04-01"])
		self.assertTrue("[2] - 19:00 (2D)" in proj)
		self.assertTrue('[1] - 19:10 (3D)' in proj)

	def test_show_places_map(self):
		seat_map = self.spells.show_places_map([])
		test_map = [
				[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
				['1', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['5', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['7', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['9', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
			]

		self.assertEqual(test_map, seat_map)

		seat_map = self.spells.show_places_map([(1,1), (5,5)])
		test_map = [
				[' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
				['1', 'X', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['2', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['3', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['4', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['5', '.', '.', '.', '.', 'X', '.', '.', '.', '.', '.'],
				['6', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['7', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['8', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['9', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
				['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
			]
		self.assertEqual(test_map, seat_map)

	def test_show_projection_reservertion(self):
		output = self.spells.show_projection_reservertion(1)

		self.assertTrue("Projections for movie 'The Hunger Games: Catching Fire' :" in output)
		self.assertTrue('[2] - 2014-04-01 19:00 (2D) - 100 spots available' in output)
		self.assertTrue('[1] - 2014-04-01 19:10 (3D) - 97 spots available' in output)
		self.assertTrue('[3] - 2014-04-02 21:00 (4DX) - 98 spots available' in output)


	def test_z(self):
		os.remove("test1.db")


if __name__ == '__main__':
    unittest.main()
import unittest
import sqlite3
import os
from os import path, remove
from magic_spells import Spells
from cinema import Cinema

class MyTests(unittest.TestCase):
	def setUp(self):
		self.cinema = Cinema("test1.db")

	def tearDown(self):
	 	self.cinema.exit()
	 	os.remove("test1.db")

	def test_add_movie(self):
		self.cinema.add_movie('The Hunger Games: Catching Fire', 7.9)
		self.cinema.cursor.execute('SELECT * FROM Movies')
		movie = self.cinema.cursor.fetchall()[0]
		self.assertTrue(movie[0] == 1)
		self.assertEqual(movie[1], "The Hunger Games: Catching Fire")
		self.assertEqual(movie[2], 7.9)

	def test_add_proj(self):
		proj = (1, 1, '3D',  '2014-04-01', '19:10')
		self.cinema.add_projection(1, '3D',  '2014-04-01', '19:10')
		self.cinema.cursor.execute('SELECT * FROM Projections')
		projection_from_db = self.cinema.cursor.fetchall()[0]
		self.assertEqual(proj, projection_from_db)

	def test_add_reservation(self):
		reservation = (1, 'RadoRado', 1, 2, 1)
		self.cinema.add_reservation('RadoRado', 1, 2, 1)
		self.cinema.cursor.execute('SELECT * FROM Reservations')
		reservation_from_db = self.cinema.cursor.fetchall()[0]
		self.assertEqual(reservation, reservation_from_db)

	def test_cancel_reservation(self):
		self.cinema.add_reservation('RadoRado', 1, 2, 1)
		self.cinema.add_reservation('RadoRado', 1, 3, 5)
		self.cinema.add_reservation('RadoRado', 1, 7, 8)
		self.cinema.add_reservation('Ivo', 3, 1, 1)
		self.cinema.add_reservation('Ivo', 3, 1, 2)
		self.cinema.add_reservation('Mysterious', 5, 2, 3)
		self.cinema.add_reservation('Mysterious', 5, 2, 4)
		self.cinema.cancel_reservation("a")
		self.cinema.cancel_reservation("RadoRado")
		testing_value = self.cinema.free_place_for_projection(1)
		self.assertEqual(testing_value, 100)


if __name__ == '__main__':
    unittest.main()
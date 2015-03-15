import sqlite3
from datetime import datetime, date

insert_movie_query = '''INSERT INTO Movies(name, rating) VALUES(?,?)'''
insert_projection_query = '''INSERT INTO Projections(movie_id, type, date, time) VALUES (?, ?, ?, ?)'''
insert_reservation_query = '''INSERT INTO Reservations(username, projection_id, row, col) VALUES (?, ?, ?, ?)'''

db = sqlite3.connect('cinema.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE Movies(id INTEGER PRIMARY KEY, name TEXT, rating INTEGER)''')

cursor.execute(insert_movie_query, ('The Hunger Games: Catching Fire', 7.9))

cursor.execute(insert_movie_query, ('Wreck-It Ralph', 7.8))

cursor.execute(insert_movie_query, ('Her', 8.3))



cursor.execute('''CREATE TABLE Projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT, date date, time ,
	FOREIGN KEY(movie_id) REFERENCES Movies(id))''')

cursor.execute(insert_projection_query, (1, '3D', '2014-04-01',	'19:10'))

cursor.execute(insert_projection_query, (1, '2D', '2014-04-01',	'19:00'))

cursor.execute(insert_projection_query, (1, '4DX', '2014-04-02', '21:00'))

cursor.execute(insert_projection_query, (3, '2D', '2014-04-05', '20:20'))

cursor.execute(insert_projection_query, (2, '3D', '2014-04-02', '22:00'))

cursor.execute(insert_projection_query, (2, '2D', '2014-04-02', '19:30'))




cursor.execute('''CREATE TABLE Reservations
		(id INTEGER PRIMARY KEY, username TEXT, projection_id INTEGER, row INTEGER, col INTEGER, 
			FOREIGN KEY(projection_id) REFERENCES Projections(id))''')

cursor.execute(insert_reservation_query, ('RadoRado', 1, 2, 1))

cursor.execute(insert_reservation_query, ('RadoRado', 1, 3, 5))
cursor.execute(insert_reservation_query, ('RadoRado', 1, 7, 8))
cursor.execute(insert_reservation_query, ('Ivo', 3, 1, 1))
cursor.execute(insert_reservation_query, ('Ivo', 3, 1, 2))
cursor.execute(insert_reservation_query, ('Mysterious', 5, 2, 3))

cursor.execute(insert_reservation_query, ('Mysterious', 5, 2, 4))

db.commit()
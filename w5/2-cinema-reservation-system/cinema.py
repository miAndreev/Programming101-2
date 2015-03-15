import sqlite3

class Cinema():

	def __init__(self, db_name):
		self.db = sqlite3.connect(db_name)
		self.cursor = self.db.cursor()
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS Movies(id INTEGER PRIMARY KEY, name TEXT, rating INTEGER)''')
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS Projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT, 
				date date, time, FOREIGN KEY(movie_id) REFERENCES Movies(id))''')
		self.cursor.execute('''CREATE TABLE IF NOT EXISTS Reservations(id INTEGER PRIMARY KEY,
			 username TEXT, projection_id INTEGER, row INTEGER, col INTEGER,
			  FOREIGN KEY(projection_id) REFERENCES Projections(id))''')

	def add_movie(self, name, rating):
		self.cursor.execute('''INSERT INTO Movies(name, rating) VALUES(?,?)''',
				 (name, rating))
		self.db.commit()

	def add_projection(self, movie_id, type_, date_, time):
		self.cursor.execute('''INSERT INTO Projections(movie_id, type, date, time) VALUES (?, ?, ?, ?)''', 
				(movie_id, type_, date_, time))
		self.db.commit()

	def add_reservation(self, name, projection_id, row, col):
		if row <= 10 and col <= 10:
			if row > 0 and col > 0:
				self.cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
					 VALUES (?, ?, ?, ?)''', (name, projection_id, row, col))
				self.db.commit()

	def fetch_movie(self, movie_id):
		self.cursor.execute('''SELECT name, rating FROM Movies WHERE id=? ''', (movie_id,))
		movie = self.cursor.fetchall()
		return movie[0]

	def fetch_movies(self):
		self.cursor.execute('''SELECT id, name, rating FROM Movies''')
		movies = self.cursor.fetchall()
		return movies

	def fetch_movie_name(self, movie_id):
		self.cursor.execute('''SELECT name FROM Movies WHERE id=?''', (movie_id,))
		return self.cursor.fetchall()

	def fetch_projections_by_id(self, movie_id):
		self.cursor.execute('''SELECT id, date, time, type FROM Projections 
			WHERE movie_id=? ORDER BY date, time''', (movie_id,))
		rows = self.cursor.fetchall()
		return rows
		
	def fetch_projections_by_id_and_date(self, movie_id, date_p):
		self.cursor.execute('''SELECT id, time, type FROM Projections WHERE movie_id=? AND date=? ORDER BY time''', (movie_id, date_p))
		rows = self.cursor.fetchall()
		return rows	
 
	def fetch_taken_seats(self, projection_id):
		self.cursor.execute('''SELECT row, col FROM Reservations WHERE projection_id=?''', (projection_id,))
		return self.cursor.fetchall()

	def cancel_reservation(self, username):
		self.cursor.execute('''DELETE FROM Reservations WHERE username = ? ''', (username,))
		self.db.commit()

	def free_place_for_projection(self, projection_id):
		self.cursor.execute("SELECT count(*) FROM Reservations WHERE projection_id=?;", (projection_id,))
		used = self.cursor.fetchall()
		used = used[0][0]
		return 100 - int(used)

	def fetch_projection(self, projection_id):
		self.cursor.execute('''SELECT date, time, type FROM Projections WHERE id=? ''', (projection_id,))
		projections = self.cursor.fetchall()
		return projections

	def exit(self):
		self.db.commit()
		self.db.close()
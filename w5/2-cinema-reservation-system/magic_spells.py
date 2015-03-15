from cinema import Cinema

class Spells():
	#db_name = "cinema.db"
	def __init__(self, db_name):
		self.cinema = Cinema(db_name)

	def show_movie(self, movie_id):
		movie = self.cinema.fetch_movie(movie_id)
		print("%s (%f)" % movie)
		return ("%s (%f)" % movie)

	def show_movies(self):
		output = []
		movies =self.cinema.fetch_movies()
		print("Current movies:")
		for movie in movies:
			print("[%d] - %s (%f)" % movie)
			output.append("[%d] - %s (%f)" % movie)
		return output

	def show_movie_projections(self, commands):
		if len(commands) == 2:
			return(self.show_pojections_by_id(commands[1]))
		elif len(commands) == 3:
			return(self.show_pojections_by_id_and_date(commands[1], commands[2]))

	def show_pojections_by_id(self, movie_id):
		output = []
		movie = self.cinema.fetch_movie_name(movie_id)
		print("Projections for movie '%s'" % movie[0])
		projections = self.cinema.fetch_projections_by_id(movie_id)
		for projection in projections:
			print("[%d] - %s %s (%s)" % projection)
			output.append("[%d] - %s %s (%s)" % projection)
		return output
		
	def show_pojections_by_id_and_date(self, movie_id, date):
		print("Projections for movie '%s' on %s:" % 
				(self.cinema.fetch_movie_name(movie_id)[0][0], date))
		output = []
		projections = self.cinema.fetch_projections_by_id_and_date(movie_id, date)
		for projection in projections:
			print("[%d] - %s (%s)" % projection)
			output.append("[%d] - %s (%s)" % projection)
		return output

	def show_places_map(self, taken_seats):
		map_seats = [
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

		for seat in taken_seats:
			map_seats[seat[0]][seat[1]] = 'X'

		return map_seats

	def show_projection(self, projection_id):
		projection = self.cinema.fetch_projection(projection_id)
		projection = projection[0]
		print(len(projection))
		print("Date and Time: %s %s (%s)" % (projection[0], projection[1], projection[2]))

	def show_projection_reservertion(self, movie_id):
		output = ["Projections for movie '%s' :" % self.cinema.fetch_movie_name(movie_id)[0][0],]
		print("Projections for movie '%s' :" % self.cinema.fetch_movie_name(movie_id)[0][0])

		projections = self.cinema.fetch_projections_by_id(movie_id)

		for projection in projections:
			print("[%d] - %s %s (%s) - %d spots available" % 
						(projection[0], projection[1], projection[2], projection[3],
							self.cinema.free_place_for_projection(projection[0])))
			output.append("[%d] - %s %s (%s) - %d spots available" % 
						(projection[0], projection[1], projection[2], projection[3],
							self.cinema.free_place_for_projection(projection[0])))

		return output

	def show_reservation_info(self, movie_id, projection_id, seats):
		print("This is your reservation:")
		self.show_movie(movie_id)
		self.show_projection(projection_id)
		print(seats)
		fin = input("Step 5 (Confirm - type 'finalize')>")
		return fin

	def cancel_reservation(self, username):
		self.cinema.cancel_reservation(username)

	def get_user_info_prompt(self):
		name = input("Step 1 (User): Choose name>")
		if name == "give_up":
			return "give_up"
			
		while True:
			tickets_number = input("Step 1 (User): Choose number of tickets>")
			if tickets_number == "give_up":
				return "give_up"
			elif tickets_number.isdigit():
				break
			else:
				print("wrong input")

		return (name, tickets_number)		

	def choose_movie_prompt(self):
		while True:
			movie_id = input("Step 2 (Movie): Choose a movie>")
			if movie_id == "give_up":
				return "give_up"
			elif movie_id.isdigit(): 
				return movie_id

	def choose_projection_prompt(self, movie_id):

		projections = self.cinema.fetch_projections_id(movie_id)

		while True:
			projection = input("Step 3 (Projection): Choose a projection>")
			if projection == "give_up":
				return "give_up"
			elif projection.isdigit():#projection in projections:
				return projection 

	def str_to_tupul(self, string):
		string = string[1:].replace(")", "")
		result_list = string.split(",")
		return (int(result_list[0]), int(result_list[1]))


	def chose_seats(self, tickets_number, projection):
		not_free_seats = self.cinema.fetch_taken_seats(projection)
		choosen_seats = []
		print("Available seats (marked with a dot):")
		#print(self.show_places_map(not_free_seats))
		seat_map = []
		for line in self.show_places_map(not_free_seats):
			#print(line)
			seat_map.append(" ".join(line))

		print("\n".join(seat_map))

		while len(choosen_seats) < tickets_number:
			
			seat = input("Step 4 (Seats): Choose seat %s>" % str(len(choosen_seats)+1))
			if seat == "give_up":
				return "give_up"
			seat = self.str_to_tupul(seat)
			if seat in not_free_seats or seat in choosen_seats:
				print("This seat is already taken!")
			elif seat[0] > 10 or seat[1] > 10:
				print("Lol...NO!")
			else:
				choosen_seats.append(seat)
			#print(choosen_seats)

		return choosen_seats


	def reservation_prompt(self):
		user_info = self.get_user_info_prompt()
		if user_info == "give_up":
			return "give_up"

		(name, tickets_number) = user_info
		tickets_number = int(tickets_number)
		self.show_movies()

		movie_id = self.choose_movie_prompt()
		if movie_id == "give_up":
			return "give_up"

		self.show_pojections_by_id(movie_id)

		while True:
			projection = self.choose_projection_prompt(movie_id)
			if projection == "give_up":
				return "give_up"
			elif tickets_number <= self.cinema.free_place_for_projection(projection):
				break

		seats = self.chose_seats(tickets_number, projection)

		if seats == "give_up":
			return "give_up"

		fin = self.show_reservation_info(movie_id, projection, seats)

		if fin == "finalize":
			for seat in seats:
				self.make_reservation(name, projection_id, seat[0], seat[1])
			print("Thanks.")

		elif fin == "give_up":
			return "give_up"

	def exit(self):
		self.cinema.exit()
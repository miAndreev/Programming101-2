import sqlite3
from magic_spells import Spells

help_msg = ""
spells = Spells()
total_seats = 100

while 1:
	command = input(">");
	command = command.split()
	if command[0] == "show_movies":
		spells.show_movies()
	elif command[0] == "show_movie_projections" :
		spells.show_movie_projections(command)

	elif command[0] == "make_reservation":
		spells.reservation_prompt()

	elif command[0] == "cancel_reservation":
		spells.cancel_reservation(command[1])

	elif command[0] == "exit":
		spells.exit()
		break

	elif command[0] == "help":
		print(help_msg)
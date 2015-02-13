import sqlite3
 
#!/usr/bin/python

db = sqlite3.connect('company.db')
cursor = db.cursor()
while 1:
	
	command = input("command>");
	command = command.split()
	if command[0] == "list_employees":
		cursor.execute('''SELECT id, name, position FROM company''')
		employees = cursor.fetchall()
		for row in employees:
			print("%d - %s - %s" %(row[0], row[1], row[2]))

	elif command[0] == "monthly_spending":
		cursor.execute('''SELECT SUM(monthly_salary) FROM company''')
		monthly_spending = cursor.fetchone()
		
		print ("The company is spending $%d every month!"% monthly_spending)

	elif command[0] == "yearly_spending":
		cursor.execute('''SELECT SUM(monthly_salary) FROM company''')
		monthly_spendings = cursor.fetchone()[0]
		yearly = monthly_spendings * 12
		cursor.execute('''SELECT SUM(yearly_bonus) FROM company''')
		bonuses = cursor.fetchone()[0]
		yearly_spending = yearly + bonuses
		print ("The company is spending $%d every year!" % yearly_spending)

	elif command[0] == "add_employee":	
		name = input("name>");
		monthly_salary = input("monthly_salary>");
		yearly_bonus = input("yearly_bonus>");
		position = input("position>");

		if monthly_salary.isdigit() and yearly_bonus.isdigit():
			cursor.execute('''INSERT INTO company(name, monthly_salary, yearly_bonus, position)
	                 VALUES(?,?,?,?)''', (name, monthly_salary, yearly_bonus, position))
			db.commit()
		else:
			print("wrong input")

	elif command[0] == "delete_employee":
		if len(command) == 2:
			if command[1].isdigit():
				cursor.execute('''SELECT name FROM company WHERE id=?''', command[1])
				name = cursor.fetchall()
				cursor.execute('''DELETE FROM company WHERE id = ? ''', command[1])
				db.commit()
				print("%s was deleted." % name[0])

	elif command[0] == "update_employee":
		if len(command) == 2:
			if command[1].isdigit():
				name = input("name>");
				monthly_salary = input("monthly_salary>");
				yearly_bonus = input("yearly_bonus>");
				position = input("position>");

				if monthly_salary.isdigit() and yearly_bonus.isdigit():
					cursor.execute('''UPDATE company SET name = ?, monthly_salary = ?,
					 yearly_bonus = ?, position = ? WHERE id = ?''',
						 (name, monthly_salary, yearly_bonus, position, command[1]))
					db.commit()
				else:
					print("wrong input")


	elif command[0] == "exit":
		break
	else:
		print("wrong command")
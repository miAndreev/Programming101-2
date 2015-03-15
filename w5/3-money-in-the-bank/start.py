import sql_manager
import re
import hashlib
import uuid
import getpass
import smtplib

admin_mail = ""
admin_pass = ""
smtp_server = "smtp.gmail.com:587"

def main_menu():
    if admin_mail == "" or smtp_server == "":
        print("config admin mail in source of start.py")
        return 0

    print("Welcome to our bank service. You are not logged in. \nPlease register or login \n to see all commands use help")
    
    while True:
        command = input("$$$>")
        
        if command == 'register':
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = get_new_pass(username)
            
            sql_manager.register(username, password, email)
            
            print("Registration Successfull")
        
        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass(prompt='Enter your password: ') 

            logged_user = sql_manager.login(username, password)

            if isinstance(logged_user, str):
                print(logged_user)
            elif logged_user != False:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif "send-reset-password" in command:
            command = command.split(" ")[1]
            if len(command) == 1:
                username = input("Enter your username: ")
            else:
                username = command[1]

            send_reset_pass(username)

        elif "reset-password" in command:
            command = command.split(" ")[1]
            if len(command) == 1:
                username = input("Enter your username: ")
            else:
                username = command[1]

            reset_pass(username)

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("send-reset-password - for sending pass reset pass email")
            print("reset_pass - for entering the pass change verification code")
            print("exit - for closing program!")

        elif command == 'exit':
            break
            
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass(prompt = "Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)
        
        elif command == 'show-message':
            print(logged_user.get_message())   

        elif command == "deposit":
            amount = input("Enter amount: ")
            tan = input("Enter TAN code: ")
            is_correct_tan = sql_manager.check_tan(logged_user.get_username(), tan)
            if is_correct_tan:
                sql_manager.deposit(logged_user.get_username(), amount)
                print ("Transaction successful!")
                print ("%s were deposited to the bank" % amount)
                new_balance = sql_manager.get_balance(logged_user.get_username())
                logged_user.update_balance(new_balance)
            else:
                print("Incorrect or invalid TAN")

        elif command == "withdraw":
            amount = input("Enter amount: ")
            tan = input("Enter TAN code: ")
            is_correct_tan = sql_manager.check_tan(logged_user.get_username(), tan)
            if is_correct_tan:
                status = sql_manager.withdraw(logged_user.get_username(), amount)
                print(status)
                new_balance = sql_manager.get_balance(logged_user.get_username())
                logged_user.update_balance(new_balance)
            else:
                print("Incorrect or invalid TAN")


        elif command == 'transaction':
            recipient = input("send to:")
            amount = input("amount:")
            if amount > logged_user.get_balance():
                print ("Not enougth money in account")
            else:
                sql_manager.make_transaction(logged_user.get_username(), recipient, amount)
                new_balance = sql_manager.get_balance(logged_user.get_username())
                logged_user.update_balance(new_balance)
                print("Done!")

        elif "get-tan" in command:
            count_tans = sql_manager.count_tans(logged_user.get_username())
            if count_tans == 0:
                password = getpass.getpass(prompt='Enter your password: ')
                send_tans(logged_user.get_username())
            else:
                print("You have %d remaining TAN for use" % count_tans)


        elif command == "del-tan":
            sql_manager.del_tan(logged_user.get_username())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("deposit - for depositing money on your account")
            print("withdraw - for withdraw from your account")
            print("transaction - for transaction between accounts")
            print("get-tan - for sending new TANs")
            print("logout or exit - for logout")

        elif command == 'exit' or command == "logout":
            break

def check_pass(password, username):
    if len(password) < 8:
        return False
    if re.match(".*\d+.*", password) == None:
        return False
    if re.match(".*[A-Z]+.*", password) == None:
        return False
    if re.match(".*[^A-Za-z0-9]+.*", password) == None:
        return False

    if username in password:
        return False

    return True

def get_new_pass(username):
    good_pass = False
    while not good_pass:
        password = getpass.getpass(prompt='Enter your new password: ') 
        good_pass = check_pass(password, username)

    return password

def send_mail(username, mail): 
    user_mail = sql_manager.get_email(username)

    if admin_pass == "":
        admin_pass = getpass.getpass(prompt = "admin email pass: ")

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(admin_usr, admin_pass)

    mail = mail %(admin_usr, user_mail)
    server.sendmail(admin_usr, user_mail, mail)
    server.quit()

def send_reset_pass(username):
    pass_recovery_hash = sql_manager.generate_pass_recovery_entry(username)

    header = """From: %s\nTo: %s\n """

    body = """Subject: Password recovery\n\n
            Use this hash to recover your pass in \"money in the bank\":\n
            %s """ % pass_recovery_hash
    mail = header + body

    send_mail(username, mail)
    print("E-mail whith verification code is send")

def reset_pass(username):
    mail = input("Enter your e-mail >")
    pass_recovery_hash = input("Enter hash to recover your password\n>")
    if correct_recovery_hash(username, mail, pass_recovery_hash):
        password = get_new_pass(username)
        sql_manager.recovery_change_pass(username, mail, password)
        print("Password is changed")
    else:
        print("Wrong username, e-mail and/or hash")

def send_tans(username):
    tans = []
    for i in range(10):
        #tan = 
        tans.append(sql_manager.generate_tan(username))

    header = """From: %s\nTo: %s\n """

    body = """Subject: New TANs\n\nYour 10 new TANs:\n%s """ % "\n".join(tans)

    mail = header + body

    send_mail(username, mail)



def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()

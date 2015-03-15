#import requests
import sqlite3
from Client import Client
import uuid
import hashlib
from datetime import datetime,  timedelta
import smtplib

conn = sqlite3.connect("bank.db", detect_types = sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                salt TEXT,
                email TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''
    cursor.execute(create_query)

    create_query = '''create table if not exists
        failed_logins(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                date timestamp
                )'''
    cursor.execute(create_query)

    create_query = '''create table if not exists
        pass_recovery(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                email TEXT,
                hash TEXT
                )'''
    cursor.execute(create_query)

    create_query = '''create table if not exists
        tans(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                tan TEXT
                )'''

    cursor.execute(create_query)

def change_message(new_message, logged_user):
    new_message = str(new_message)
    logged_user_id = str(logged_user.get_id())
    update_sql = "UPDATE clients SET message = ? WHERE id = ?" 
    cursor.execute(update_sql, (new_message, logged_user_id)) 
    conn.commit()
    logged_user.set_message(new_message)

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return (hashlib.sha256(salt.encode() + password.encode()).hexdigest(), salt)

def change_pass(new_pass, logged_user):
    password, salt = hash_password(new_pass)
    update_sql = "UPDATE clients SET password = ?, salt = ? WHERE id = ?" 
    cursor.execute(update_sql, (password, salt, logged_user.get_id()))
    conn.commit()

def recovery_change_pass(user_mail, username, new_pass):
    password, salt = hash_password(new_pass)
    update_sql = "UPDATE clients SET password = ?, salt = ? WHERE username = ? AND email = ?" 
    cursor.execute(update_sql, (password, salt, username, user_mail))
    conn.commit()

def register(username, password, email):
    insert_sql = "insert into clients (username, email, password, salt) values (?, ?, ?, ?)"
    password, salt = hash_password(password)
    cursor.execute(insert_sql, (username, email, password, salt))
    conn.commit()

def check_password(hash_and_salt, user_password):
    password, salt = hash_and_salt
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def login(username, password):
    select_query = "SELECT id, username, balance, message, email FROM clients WHERE username = ? AND password = ? LIMIT 1" 
    select_query_get_salt = "SELECT salt FROM clients WHERE username = ?" # LIMIT 1" 
    exists_user_query = "SELECT COUNT(*) FROM clients WHERE username = ?"
    cursor.execute(exists_user_query, (username,))
    user_count = cursor.fetchone()[0]
    if user_count >= 1: 
        if not is_blocked(username):
            
            cursor.execute(select_query_get_salt, (username,))
            salt = cursor.fetchone()
            if salt == None:
                
                return False
            else:
                salt = salt[0]

            hashed_pass = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
            cursor.execute(select_query, (username, hashed_pass))
            user = cursor.fetchone()

            if(user):
                return Client(user[0], user[1], user[2], user[3], user[4])
            else:
                
                faild_login_count_up(username)
                return False
        else:
            return "Too many login fails! Try again later!"
    else:
        return False

def faild_login_count_up(username):
    insert_sql = "insert into failed_logins (username, date) values (?, ?)"
    date = datetime.now() 
    cursor.execute(insert_sql, (username, date))
    conn.commit()

def is_blocked(username):
    clean_db_query = "DELETE FROM failed_logins WHERE date < datetime('now','+30 minutes')"
    select_query = "SELECT COUNT(*) FROM failed_logins WHERE username = ?"
    select_query_get_all = "SELECT date FROM failed_logins WHERE username = ? ORDER BY date DESC"
    cursor.execute(select_query, (username,))
    failed_logins_count = cursor.fetchone()[0]
    if failed_logins_count >= 5:
        cursor.execute(select_query_get_all, (username,))
        last_failed_login = cursor.fetchone()[0]
        cursor.execute(clean_db_query)
        bann_end = last_failed_login + timedelta(minutes = 5)
        time_diff = bann_end - datetime.now() 
        conn.commit()

        if time_diff.days >= 0:
            return True

    return False

def generate_pass_recovery_entry(username, mail):
    pass_recovery_hash = uuid.uuid4().hex
    insert_sql = "insert into pass_recovery (username, email, hash) values (?, ?, ?)"
    cursor.execute(insert_sql, (username, mail, pass_recovery_hash))
    conn.commit()
    return pass_recovery_hash

def correct_recovery_hash(username, mail, pass_recovery_hash):
    count_query = "SELECT COUNT(*) FROM pass_recovery WHERE username = ? AND email = ? AND hash = ?"
    delete_query = "DELETE FROM pass_recovery WHERE username = ? AND email = ? AND hash = ?"

    cursor.execute(count_query, (username, mail, pass_recovery_hash))
    count = cursor.fetchone()[0]

    if count == 0:
        return False

    else:
        cursor.execute(delete_query, (username, mail, pass_recovery_hash))
        conn.commit()
        return True

def user_exist(username):
    exist_query = "SELECT COUNT(*) FROM clients WHERE username = ?"

    cursor.execute(exist_query, (username,))
    count = cursor.fetchone()[0]
    if count == 1:
        return True

    else:
        return False

def change_balance(username, balance):
    change_balance_query = "UPDATE clients SET balance = ? WHERE username = ? "
        
    cursor.execute(change_balance_query,(balance,username))
    conn.commit()

def get_email(username):
    select_query = "SELECT email FROM clients WHERE username = ? " 

    cursor.execute(select_query, (username,))
    email = cursor.fetchone()[0]

    return email

def get_balance(username):
    select_query = "SELECT balance FROM clients WHERE username = ? " 

    cursor.execute(select_query, (username,))
    balance = cursor.fetchone()[0]

    print("balance of user %s is %f" %(username, balance))

    return balance

def make_tansaction(sender, recipient, amount):
    withdraw_status = withdraw(sender, amount) 
    
    if withdraw_status == "Done":
        deposit(recipient, amount)
    
    return withdraw_status

def deposit(username, amount):
    change_balance(username, get_balance(username) + float(amount))

def withdraw(username, amount):
    amount = float(amount)
    balance = get_balance(username)
    if balance >= amount:
        change_balance(username, balance - amount)
        return "Done"
    else:
        return "You balance is not enought"

def generate_tan(username):
    tan = uuid.uuid4().hex
    create_query = "insert into tans (username, tan) values (?, ?)"

    cursor.execute(create_query, (username, tan))
    conn.commit()

    return tan


def check_tan(username, tan):
    select_query = "SELECT COUNT(*) FROM tans WHERE username = ? AND tan = ?"
    delete_query = "DELETE FROM tans WHERE username = ? AND tan = ?"
    cursor.execute(select_query, (username, tan))
    found_matches = cursor.fetchone()[0]
    if found_matches >= 1:
        cursor.execute(delete_query, (username, tan))
        conn.commit()
        return True

    return False

def count_tans(username):
    select_query = "SELECT COUNT(*) FROM tans WHERE username = ?"
    cursor.execute(select_query, (username,))
    count = cursor.fetchone()[0]
    return count

def del_tan(username):
    delete_query = "DELETE FROM tans WHERE username = ? "
    cursor.execute(delete_query, (username,))
    conn.commit()



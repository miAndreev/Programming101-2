import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        salt = '2528cdecb0c8469dbe4171a539f58ff7'
        password = "e4379c8151ac5c3bcc8c6f9ec9d8e09d672e8ebc4caf79138386914f121c88de"
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123', "a@b.cc")

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')
        sql_manager.cursor.execute('DROP TABLE failed_logins')
        sql_manager.cursor.execute("DROP TABLE pass_recovery")
        sql_manager.cursor.execute("DROP TABLE tans")

    def test_register(self):
        sql_manager.register('Dinko', '123123', "a@b.cc")

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?)', ('Dinko',))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login("Tester", '123')
        self.assertEqual(logged_user.get_username(), 'Tester')
        self.assertEqual(logged_user.get_email(), "a@b.cc")

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_multiple_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123')
    
        self.assertEqual(logged_user, "Too many login fails! Try again later!")

    def test_multiple_login_wrong_password1(self):
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123567')
        logged_user = sql_manager.login('Tester', '123')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_multiple_usr_one_name(self):
        pass
        # when there is more users with same username the login fails
        # sql_manager.register('Tester1', 'abCD1!jgs', "aa@b.cc")
        # sql_manager.register('Tester1', 'abCD1!jga', "ab@b.cc")
        # logged_user = sql_manager.login("Tester1", "abCD1!jgj")
        # self.assertEqual(logged_user.get_email(), 'ab@b.cc')
        # logged_user = sql_manager.loggin("Tester1", "abCD1!jgs")
        # self.assertEqual(logged_user.get_email(), 'aa@b.cc')

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', '123')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', '123')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_sql_injection(self):
        injection = "' OR 1 = 1 --"
        password = "abc"
        logged_user = sql_manager.login(injection, password)
        self.assertFalse(logged_user)

    def test_generate_recovery_entry(self):
        sql_manager.generate_pass_recovery_entry('Tester', "a@b.cc")
        sql_manager.cursor.execute('SELECT email FROM pass_recovery WHERE username = (?)', ('Tester',))
        entry = sql_manager.cursor.fetchone()[0]
        self.assertTrue("a@b.cc" in entry)

    def test_recover_pass(self):
        recovery = sql_manager.generate_pass_recovery_entry('Tester', "a@b.cc")
        correct_hash = sql_manager.correct_recovery_hash('Tester', "a@b.cc", recovery)
        self.assertTrue(correct_hash)

    def test_usr_exist(self):
        self.assertTrue(sql_manager.user_exist('Tester'))
        self.assertFalse(sql_manager.user_exist('Tester1'))

    def test_change_balance(self):
        sql_manager.change_balance("Tester", 2)
        sql_manager.cursor.execute('SELECT balance  FROM clients WHERE username = (?)', ('Tester',))
        new_balance = sql_manager.cursor.fetchone()[0]
        self.assertEqual(new_balance, 2.0)

    def test_get_balance(self):
        balance = sql_manager.get_balance("Tester")
        self.assertEqual(balance, 0)

    def test_transaction(self):
        sql_manager.change_balance("Tester", 100)
        sql_manager.register('Tester2', '123', "a@b.cc")
        sql_manager.make_tansaction("Tester", "Tester2", 10)
        self.assertEqual(sql_manager.get_balance("Tester"), 90.0)
        self.assertEqual(sql_manager.get_balance("Tester2"), 10.0)

    def test_deposit(self):
        sql_manager.deposit("Tester", 100)
        new_balance = sql_manager.get_balance("Tester")
        self.assertEqual(new_balance, 100.0)

    def test_withdraw(self):
        sql_manager.deposit("Tester", 100)
        sql_manager.withdraw("Tester", 10)
        new_balance = sql_manager.get_balance("Tester")
        self.assertEqual(new_balance, 90.0)

    def test_count_tans(self):
        self.assertEqual(sql_manager.count_tans("Tester"), 0)
        sql_manager.generate_tan("Tester")
        self.assertEqual(sql_manager.count_tans("Tester"), 1)
        sql_manager.generate_tan("Tester")
        sql_manager.generate_tan("Tester")
        sql_manager.generate_tan("Tester1")
        self.assertEqual(sql_manager.count_tans("Tester"), 3)

    def test_gen_tan(self):
        sql_manager.generate_tan("Tester")
        sql_manager.cursor.execute('SELECT Count(*)  FROM tans WHERE username = ?', ('Tester',))
        tans_count = sql_manager.cursor.fetchone()[0]
        self.assertEqual(tans_count, 1)

    def test_check_tan(self):
        tan = sql_manager.generate_tan("Tester")
        sql_manager.cursor.execute('SELECT Count(*)  FROM tans WHERE username = ?', ('Tester',))
        tans_count = sql_manager.cursor.fetchone()[0]
        self.assertEqual(tans_count, 1)
        self.assertTrue(sql_manager.check_tan("Tester", tan))
        sql_manager.cursor.execute('SELECT Count(*)  FROM tans WHERE username = ?', ('Tester',))
        tans_count = sql_manager.cursor.fetchone()[0]
        self.assertEqual(tans_count, 0)




if __name__ == '__main__':
    unittest.main()

import unittest

import bcrypt

from access_control_constants import AccessSubjects
from main import save_password, get_password_record, password_checker


class TestMain(unittest.TestCase):
    def test_save_password(self):
        """ Tests the save_password method in main.py

        :return: None
        """
        username_expected = "testUser"
        password_expected = "testPassword13!"
        role_expected = AccessSubjects.Tellers.value
        record_length_expected = 3

        save_password(username_expected, password_expected, role_expected)

        username_actual = ""
        password_actual = ""
        role_actual = ""
        record_length_actual = 0

        file1 = open("passwd.txt", "r")
        for file_record in file1:
            record = file_record.strip().split(":")
            if record[0] == username_expected:
                username_actual = record[0]
                password_actual = record[1]
                role_actual = record[2]
                record_length_actual = len(record)
                file1.close()
                break

        self.assertEqual(username_expected, username_actual)
        self.assertTrue(bcrypt.checkpw(password_expected.encode(), password_actual.encode()))
        self.assertEqual(role_expected, role_actual)
        self.assertEqual(record_length_expected, record_length_actual)

    def test_get_password_record(self):
        """ Tests the get_password_record method in main.py

        :return: None
        """
        username_expected = "testUserGetPassword"
        password_expected = "getPassword2!"
        role_expected = AccessSubjects.ComplianceOfficers.value

        file1 = open("passwd.txt", "a")
        password_record_expected = username_expected + ":" + password_expected + ":" + role_expected + "\n"
        file1.write(password_record_expected)
        file1.close()

        password_record_actual = get_password_record(username_expected)

        password_record_expected_list = password_record_expected.strip().split(":")
        self.assertEqual(password_record_expected_list, password_record_actual)

    def test_password_checker(self):
        """ Test password_checker method in main.py

        :return: None
        """

        # Test case 1
        username = "SYSC1"
        pasword = "Sysc48!"
        self.assertFalse(password_checker(username, pasword))

        # Test case 2
        username = "SYSC2"
        pasword = "Sysc4810b113!"
        self.assertFalse(password_checker(username, pasword))

        # Test case 3
        username = "SYSC3"
        pasword = "sysc4810!"
        self.assertFalse(password_checker(username, pasword))

        # Test case 4
        username = "SYSC4"
        pasword = "SYSC4810!"
        self.assertFalse(password_checker(username, pasword))

        # Test case 5
        username = "SYSC5"
        pasword = "Sysccarl!"
        self.assertFalse(password_checker(username, pasword))

        # Test case 6
        username = "SYSC6"
        pasword = "Sysc4810"
        self.assertFalse(password_checker(username, pasword))

        # Test case 7
        username = "SYSC7"
        pasword = "Qwerty123"
        self.assertFalse(password_checker(username, pasword))

        # Test case 8
        username = "Sysc4810!"
        pasword = "QWERTY123"
        self.assertFalse(password_checker(username, pasword))

        # Test case 9
        username = "SYSC9"
        pasword = "SYSC4810!"
        self.assertFalse(password_checker(username, pasword))
        # Test case 10
        username = "SYSC10"
        pasword = "2001-12-01"
        self.assertFalse(password_checker(username, pasword))

        # Test case 11
        username = "SYSC11"
        pasword = "amc-313"
        self.assertFalse(password_checker(username, pasword))

        # Test case 12
        username = "SYSC12"
        pasword = "613-850-1212"
        self.assertFalse(password_checker(username, pasword))

        # Test case 13
        username = "SYSC13"
        pasword = "Sysc4810!"
        self.assertTrue(password_checker(username, pasword))


if __name__ == '__main__':
    unittest.main()

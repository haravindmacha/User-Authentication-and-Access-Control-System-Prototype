# This is a sample Python script.
import access_control_constants
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from access_control_matrix import *

import bcrypt
import re


def save_password(username, password, role) -> None:
    """ Adds records to the password file

    :param username: username of the user
    :param password: password of the user
    :param role: the role of the user in the system
    :return: None
    """
    password_bytes = password.encode('utf-8')
    # generating the salt
    salt = bcrypt.gensalt()
    # Hashing the password
    bcrypt_hash = bcrypt.hashpw(password_bytes, salt)
    string_hash = bcrypt_hash.decode('utf-8')

    file1 = open("passwd.txt", "a")
    password_record = username + ":" + string_hash + ":" + role + "\n"
    file1.write(password_record)
    file1.close()


def get_password_record(username) -> list:
    """ Retrieves a record from the password file, based of the username

    :param username: username specified by user
    :return: record from the password file
    """

    file1 = open("passwd.txt", "r")

    for file_record in file1:
        # gets singular record with \n at the end
        record = file_record.strip().split(":")
        if record[0] == username:
            file1.close()
            return record

    file1.close()
    return []


def password_checker(username, password) -> bool:
    """ checks if the password entered, is 8-12 characters, contains at least one uppercase letter, lower case
    letter, numerical digit and one special character, the password isn't on the list of common weak passwords,
    the password isnt int eh fromat of common numbers scuh as dates and license plates, and the password isnt the
    username

    :param username: the username entered by the user
    :param password: The potential password entered by the user
    :return: true if the password adheres the password policy, false if not
    """

    common_weak_password = ["Password1", "Qwerty123", "Qaz123wsx"]
    special_characters = "!@#$%?*"

    common_number_formats = []
    calendar_dates_format1 = "^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"
    calendar_dates_format2 = "^[0-9][0-9]/[0-9][0-9]/[0-9][0-9]"
    license_plate_numbers_format = "^[a-zA-Z][a-zA-Z][a-zA-Z]-[0-9][0-9][0-9]"
    telephone_numbers_format = "^[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]"

    common_number_formats.append(calendar_dates_format1)
    common_number_formats.append(calendar_dates_format2)
    common_number_formats.append(license_plate_numbers_format)
    common_number_formats.append(telephone_numbers_format)

    if len(password) > 12 or len(password) < 8:
        return False
    # checks if password doesnt contain a capital letter
    elif re.search('[A-Z]', password) is None:
        return False
    # checks if password doesnt contain a lowercase letter
    elif re.search('[a-z]', password) is None:
        return False
    # checks if password doesnt contain a number
    elif re.search('[0-9]', password) is None:
        return False
    # checks if password doesnt contain a special character
    elif not any(character in special_characters for character in password):
        return False
    # checks if password is ome of the common weak passwords
    elif password.lower() in [common_passwords.lower() for common_passwords in common_weak_password]:
        return False
    # checks if password format matches a common number format
    elif any(re.search(common_format, password) is not None for common_format in common_number_formats):
        return False
    # checks if password is same as username
    elif username.lower() == password.lower():
        return False
    else:
        # if none of the negative conditionals is found, then password adheres to the policy
        return True


def enroll_users() -> None:
    """ user interface to allow for users to ernrol users to the system

    :return: None
    """
    print("\nHello, welcome to the Finvest Holdings enrollment")

    # while loop for user to enter username until they enter an appropriate username
    while True:
        username = input("please enter a username:")

        # checks if the username is not only whitespace and if the username is unique in the password file
        if len(get_password_record(username)) == 0 and not username.isspace():
            break
        else:
            print("This username can not be selected")

    print("time to select a role \nEnter 1 for Client role \nEnter 2 for Premium Client role \n"
          "Enter 3 for Financial Planner role \nEnter 4 for Financial Advisor role \n"
          "Enter 5 for Investment Analyst role \nEnter 6 for Technical Support role \nEnter 7 for Teller role \n"
          "Enter 8 for Compliance Officer role")

    # while loop for user to select a role until they enter an appropriate input
    while True:
        role_input = input("Please enter you choice here:")

        # Gets the role of the user based of the number inputed
        if role_input == "1":
            role = AccessSubjects.Clients.value
            break
        elif role_input == "2":
            role = AccessSubjects.PremiumClients.value
            break
        elif role_input == "3":
            role = AccessSubjects.FinPlanners.value
            break
        elif role_input == "4":
            role = AccessSubjects.FinAdvisors.value
            break
        elif role_input == "5":
            role = AccessSubjects.InvestAnalyst.value
            break
        elif role_input == "6":
            role = AccessSubjects.TechSupport.value
            break
        elif role_input == "7":
            role = AccessSubjects.Tellers.value
            break
        elif role_input == "8":
            role = AccessSubjects.ComplianceOfficers.value
            break
        else:
            print("You did not select one of the options above")

    # while loop for user to enter password until they enter an appropriate password
    while True:
        password = input("please enter a password:")
        # check if password entered adheres to password policy
        if password_checker(username, password):
            save_password(username, password, role)
            break
        else:
            print("Password doesnt match all the requirements")

    print("Done Creating Your Account")


def login_users() -> None:
    """ user interface to allow for users to login to the system

    :return: None
    """
    print("\nHello, welcome to the Finvest Holdings login")

    # while loop for user to enter username and password until they enter an appropriate username, password combination
    while True:
        username = input("please enter your username:")
        password = input("please enter your password:")
        password_record = get_password_record(username)

        # checks if the username is only whitespace or if the username doesn't exist in the password file
        if len(password_record) == 0 or username.isspace():
            print("Incorrect username or password \n")
        else:
            # case where username is in the file
            actual_password = password_record[1]
            # checks if the password entered is equal to hashed password in the password file
            if bcrypt.checkpw(password.encode(), actual_password.encode()):
                print("\nAccess Granted")
                access_control_matrix = AccessControlMatrix()
                print("Username:" + username)
                print("Role:" + password_record[2])

                # Gets the capabilites for the user based off the role listed in the password file
                capabilities = access_control_matrix.get_capabilities(AccessSubjects(password_record[2]))
                print("List of access rights you have currently:")
                for access_object, access_type in capabilities.items():
                    print(access_type.value + " for the " + access_object.value)

                break
            else:
                print("Incorrect Username or password \n")


if __name__ == '__main__':

    print("Hello, welcome to the Finvest Holdings \nEnter 1 to enrol account \nEnter 2 to login")

    # while loop for user to select between login or enrolling they enter an appropriate choice
    while True:
        choice = input("Please enter you choice here:")
        if choice == "1":
            enroll_users()
            break
        elif choice == "2":
            login_users()
            break
        else:
            print("You did not select one of the options above")

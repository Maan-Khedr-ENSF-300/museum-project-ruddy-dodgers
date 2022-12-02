import mysql.connector
from mysql.connector import errorcode
import maskpass
from end_user import *
from admin import *
from data_entry import *


def db_connector(username, password):

    try:
        cnx = mysql.connector.connect(
            user=username, password=password, host='127.0.0.1', database='MUSEUMART')
        print("Connection Successful")

        return cnx

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Incorrect Username or Password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print("Connection Unsuccessful. Please try again.")
            print(err)


def main():
    print("Welcome to the MySQL Database Manager.")
    print("In order to proceed please select your role from the list below:\n1-DB Admin\n2-Data Entry\n3-Browse as guest")

    valid = False
    while not valid:
        selection = input("please type 1, 2, or 3 to select your role:")
        if selection in ['1', '2']:
            username = input("Username:")
            password = maskpass.askpass("Please Enter Password: ", mask='*')
        elif selection == '3':
            username = "guest"
            password = None
        else:
            print("Invalid Selection - Please try again")

        try:
            cnx = db_connector(username, password)
            cursor = cnx.cursor()
            valid = True

        except Exception:
            pass

    if selection == '1':
        admin_main_menu(cnx, cursor)
    elif selection == '2':
        entry_main_menu(cnx, cursor)
    elif selection == '3':
        browsing_main_menu(cursor)

    print("Thank you. Exited Successfully.")
    cnx.commit()
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()

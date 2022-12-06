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

    cnx, cursor = None, None
    loop = True
    while loop:

        if cnx or cursor:
            cursor.close()
            cnx.close()

        valid = False
        while not valid:
            print("\nWelcome to the MySQL Database Manager.\nIn order to proceed please select your role from the list below:\n1-DB Admin\n2-Data Entry\n3-Browse as guest\n4-Other User\n0-Quit")
            selection = input("please type 1, 2, 3, or 4 to select your role:")
            if selection == '1':
                pass
                username = 'admin'
                password = 'password'
            elif selection == '2':
                username = "data_entry"
                password = 'password'
            elif selection == '3':
                username = "guest"
                password = ''
            elif selection == '4':
                username = input("Username:")
                password = maskpass.askpass(
                    "Please Enter Password: ", mask='*')
            elif selection == '0':
                print("Exiting Program...")
                exit(1)
            else:
                print("Invalid Selection - Please try again")

            try:
                cnx = db_connector(username, password)
                cursor = cnx.cursor()
                valid = True

            except Exception:
                pass

        if selection == '1':
            loop = admin_main_menu(cnx, cursor)
        elif selection == '2':
            loop = entry_main_menu(cnx, cursor)
        elif selection == '3':
            loop = browsing_main_menu(cursor)

    print("Thank you. Exited Successfully.")
    cnx.commit()
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()

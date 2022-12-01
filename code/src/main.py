import mysql.connector
from mysql.connector import errorcode
import maskpass
from sql_operations import *


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
            print(err)


def main():
    print("Welcome to the MySQL Database Manager.")
    print("In order to proceed please select your role from the list below:\n1-DB Admin\n2-Data Entry\n3-Browse as guest")
    selection = input("please type 1, 2, or 3 to select your role:")

    if selection in ['1', '2']:
        username = input("Username:")
        password = maskpass.askpass("Please Enter Password: ", mask='*')
    else:
        username = "guest"
        password = None

    connection_unsuccessful = True
    while connection_unsuccessful:
        try:
            database = input("Database: ")
            host = input("Host: ")

            cnx = db_connector(username, password, database, host)
            cursor = cnx.cursor()
            connection_unsuccessful = False
        except Exception as e:
            print("Connection Unsuccessful. Please try again.")
            print(e)

    print("Thank you. Exited Successfully.")
    cnx.commit()
    cursor.close()
    cnx.close()


if __name__ == '__main__':
    main()

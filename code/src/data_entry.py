import pandas as pd
from helper_functions import *


def entry_main_menu(cnx, cursor):
    chosen = False
    while not chosen:
        choice = input(
            "What would you like to do:\n1. Look Up Info\n2. Insert New Data\n3. Update/Delete Tuples\n0.Quit")

        if choice == '1':
            data_lookup(cursor)

        elif choice == '2':
            table_name = chose_table(cursor)
            chosen2 = False
            while not chosen2:
                choice2 = input(
                    "Would you like to insert data manually or from a file? (M/F): ")
                if choice2 == 'M':
                    insert_manually(table_name, cursor)
                    cnx.commit()
                    chosen2 = True

                elif choice2 == 'F':
                    get_file_data(table_name, cursor)
                    cnx.commit()
                    chosen2 = True

                else:
                    print("Invalid Input. Please try again.")
                    continue

        elif choice == '3':
            table_name = chose_table(cursor)
            change_data(table_name, cursor)
            cnx.commit()

        elif choice == '0':
            chosen = True
            print("Thank you. Exited Successfully.")
            exit(1)

        else:
            print("Invalid Input. Please try again.")


def chose_table(cursor):
    c_table = False
    while not c_table:
        cursor.execute("SHOW TABLES;")
        print_table(cursor)
        rows = cursor.fetchall()
        table = input(
            "What table would you like to insert data into: ")

        if table in rows:
            c_table = True
            return table


def change_data(table_name, cursor):
    pass


def data_lookup(cursor):
    pass


def insert_manually(table_name, cursor):
    pass


def get_file_data(table_name, cursor):
    # TODO ASK PROF FOR HOW THE FILE SHOULD BE FORMATTED (SEPERATED BY SPACES OR COMMAS)
    """_summary_

    Args:
        table_name (string): The name of the table for which the data is being add to
        cursor (object): allows us to execute queries and fetch results for the chosen database

    Returns:
        df (DataFrame): pandas dataframe of the data from the file with the table columns as the column names
    """

    valid = False
    while not valid:
        file_name = input("Enter the path to the file: ")

        try:
            file = open(file_name, 'r')
            lines = [i.strip().split(' ') for i in file.readlines()]
            df = pd.DataFrame(lines)
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            df.columns = cursor.column_names

            file.close()
            valid = True
            return df

        except Exception as e:
            print("Error Opening File: ", e)

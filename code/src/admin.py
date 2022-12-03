from helper_functions import *


def admin_main_menu(cnx, cursor):
    chosen = False
    while not chosen:
        choice = input(
            "\nWhat would you like to do:\n1. Query\n2. Run SQL Script File\n3. Modify Database\n4. Edit Users\n0. Quit\n9. Log Out")

        if choice == '1':
            query(cursor)

        elif choice == '2':
            init_database(cursor)

        elif choice == '3':
            modify_database(cursor)
            cnx.commit()

        elif choice == '4':
            modify_user(cursor)
            cnx.commit()

        elif choice == '0':
            chosen = True
            return False

        elif choice == '9':
            chosen = True
            print('Logging Out!')
            return True

        else:
            print("Invalid Input. Please try again.")


def init_database(cursor):
    i = 0
    working = False
    while not working:
        file_name = input("Enter the path to the file: ")

        try:
            with open(file_name, 'r') as fd:
                sql_file = fd.read()
            sqlCommands = sql_file.split(';')
            working = True

        except Exception as e:
            print("Error Opening File: ", e)

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except Exception as e:
            print("Command skipped: ", e)
            i += 1

    print(f"Executed with {i} errors.")


def modify_user(cursor):
    # TODO ADD, EDIT, AND BLOCK USERS
    pass


def modify_database(cursor):
    pass


def query(cursor):
    """Goes through and asks for user inputs to 
    Execute a generic SQL query
    Args:
        cursor: cursor object that can used to execute queries and fetch results 
        for the chosen database
    """
    try:

        query = input("Enter the query: \n")
        cursor.execute(query)
        print_table(cursor)
        # DO WE HAVE TO PRINT THE TABLE?

    except Exception as e:
        print("\nThere was an error in your query, please try again")
        print(e)

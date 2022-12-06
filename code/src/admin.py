from helper_functions import *


def admin_main_menu(cnx, cursor):
    chosen = False
    while not chosen:
        choice = input(
            "\nWhat would you like to do:\n1. Query\n2. Run SQL Script File\n3. Modify Database\n4. Edit Users\n0. Quit\n9. Log Out\n")

        if choice == '1':
            query(cursor)
            cnx.commit()

        elif choice == '2':
            init_database(cursor)
            cnx.commit()


        elif choice == '3':
            modify_database(cursor)
            cnx.commit()

        elif choice == '4':
            modify_user(cnx, cursor)

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


def modify_user(cnx, cursor):
    # TODO ADD, EDIT, AND BLOCK USERS
    
    chosen = False
    while not chosen:
        selection = int(input("\nWhat would you like to do:\n1. Add User\n2. Edit User Privileges\n3. Manage User\n"))
        if selection == 1:
            new_user = input("Please enter the name of the new user:\n")
            user_level = input("Please type the role you would like to grant the user\n-- admin\n-- write_access\n-- read_access\n")

            cursor.execute(f"DROP USER IF EXISTS '{new_user}'@'localhost'")
            cnx.commit()
            cursor.execute(f"CREATE USER '{new_user}'@'localhost' IDENTIFIED BY 'password'")
            cnx.commit()
            cursor.execute(f"GRANT '{user_level}'@'localhost' TO {new_user}@localhost;")
            cnx.commit()
            chosen = True

        elif selection == 2:
            #Display's table of users
            cursor.execute("SELECT user FROM mysql.user WHERE NOT user in ('mysql.infoschema', 'mysql.session', 'mysql.sys', 'root') AND NOT (account_locked='Y' AND password_expired='Y' AND authentication_string='');")
            print_table(cursor)
            user = input("Please enter the name of the user:\n")

            cursor.execute(f"SHOW GRANTS FOR {user}@localhost")
            print_table(cursor)
            action = input("Would you like to Grant or Revoke a privilege:\n").upper()
            privilege = input("What Privilege would you like to perform this action on:\n").upper()

            if privilege == "GRANT":
                cursor.execute(f"{action} {privilege} ON MUSEUMART.* TO {user}@localhost")
            elif privilege == "REVOKE":
                cursor.execute(f"{action} {privilege} ON MUSEUMART.* FROM {user}@localhost")
            chosen = True
        
        elif selection == 3: 
            #Display's table of users
            cursor.execute("SELECT user, account_locked FROM mysql.user WHERE NOT user in ('mysql.infoschema', 'mysql.session', 'mysql.sys', 'root') AND NOT (account_locked='Y' AND password_expired='Y' AND authentication_string='');")
            print_table(cursor)
            user = input("Please enter the name of the user:\n")
            
            action = input("Would you like to Lock, unlock or delete user:\n").upper()

            if action == "LOCK":
                cursor.execute(f"ALTER USER {user}@localhost ACCOUNT LOCK")
                cnx.commit()
            elif action == "UNLOCK":
                cursor.execute(f"ALTER USER {user}@localhost ACCOUNT LOCK")
                cnx.commit()
            elif action == "DELETE":
                cursor.execute(f"DROP USER {user}@localhost")
                cnx.commit()
            chosen = True




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

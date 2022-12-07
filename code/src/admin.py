from helper_functions import *


def admin_main_menu(cnx, cursor):

    while True:
        choice = input(

            "\nWhat would you like to do:\n1. Query\n2. Run SQL Script File\n3. Edit Users\n0. Quit\n9. Log Out\n")

        if choice == '1':
            query(cursor)
            cnx.commit()

        elif choice == '2':
            execute_script(cursor)
            cnx.commit()

        elif choice == '3':
            modify_user(cnx, cursor)
            cnx.commit()

        elif choice == '0':
            print("Exiting Program...")
            exit(1)

        elif choice == '9':
            print('Logging Out!')
            return True

        else:
            print("Invalid Input. Please try again.")


def execute_script(cursor):
    i = 0
    working = False
    while not working:
        file_name = input("Enter the path to the file (enter q to exit menu): ")
        if file_name == 'q':
            return

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
    print_table(cursor)
 

def modify_user(cnx, cursor):

    while True:

        try:
            selection = int(input("\nWhat would you like to do:\n1. Add User\n2. Edit User Privileges\n3. Manage User\n"))
            if selection == 1:
                new_user = input("Please enter the name of the new user:\n")
                user_level = input("Please type the role you would like to grant the user\n-- db_admin\n-- write_access\n-- read_access\n")

                cursor.execute(f"DROP USER IF EXISTS '{new_user}'@'localhost'")
                cnx.commit()
                cursor.execute(f"CREATE USER '{new_user}'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'")
                cnx.commit()
                ##Adds role to 
                cursor.execute(f"GRANT '{user_level}'@'localhost' TO {new_user}@localhost;")
                cnx.commit()
                cursor.execute(f"SET DEFAULT ROLE ALL TO '{new_user}'@'localhost'")
                cnx.commit()
                break

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
                cursor.execute("FLUSH PRIVILEGES")
                break
            
        
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
                    cursor.execute(f"ALTER USER {user}@localhost ACCOUNT UNLOCK")
                    cnx.commit()
                elif action == "DELETE":
                    cursor.execute(f"DROP USER {user}@localhost")
                    cnx.commit()
                break

        except Exception as e:
                print("Error Managing Users")
                print(e)
                break

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

from helper_functions import *


def entry_main_menu(cnx, cursor):

    while True:
        choice = input(
            "What would you like to do:\n1. Look Up Info\n2. Insert New Data\n3. Update/Delete Tuples\n0. Quit\n9. Logout\n")
        if choice == '1':
            data_lookup(cursor)
        
        elif choice == '2':
            table_name = choose_table(cursor)
            while True:
                choice2 = input("Would you like to insert data manually or from a file? (M/F): ").upper()
                if choice2 == 'M':
                    insert_manually(table_name, cursor)
                    cnx.commit()
                    break
                elif choice2 == 'F':
                    get_file_data(table_name, cursor)
                    cnx.commit()
                    break
                else:
                    print("Invalid Input. Please try again.")
                    continue

        elif choice == '3':
            table_name = choose_table(cursor)
            change_data(table_name, cursor)
            cnx.commit()

        elif choice == '0':
            print("Exiting Program...")
            exit(1)

        elif choice == '9':
            print('Logging Out!')
            return True

        else:
            print("Invalid Input. Please try again.")
            continue



def data_lookup(cursor):
    """Allows User to view data inside tables
    Args: 
        cursor (object): allows us to execute queries and fetch results for the chosen database
    Returns:
        None
    """
    cursor.execute("SHOW TABLES;")
    print_table(cursor)
    choose_table(cursor)
    print_table(cursor)


def change_data(table, cursor):
    """Allows User to view data inside tables
    Summary:
        Allows User to update data inside table
    Args:
        table (str) : name of table to enter data into 
        cursor (object): allows us to execute queries and fetch results for the chosen database
    Returns:
        None
    """
    #get and display table data
    print_table(cursor)
    num_attributes = len(cursor.description)
    attribute_list = [i[0] for i in cursor.description]
    uid = input("Please enter the 3 digit ID of the item you would like to update in the database:\n")
    attribute = input("Which column would you like to update:\n")
    data = input("Enter your new value:\n")
    update_command = f"UPDATE {table} SET {attribute} = '{data}' WHERE Unique_ID = {uid}"

    print(update_command)
    try:
        cursor.execute(update_command)
    except Exception as e:
        print("Error Updating Data")
        print(e)


def insert_manually(table, cursor):
    """
    Summary:
        Allows User to manually enter data into the table
    Args:
        table (str) : name of table to enter data into
        cursor (object): allows us to execute queries and fetch results for the chosen database
    Returns:
        None
    """
    
    print_table(cursor)

    num_attributes = len(cursor.description)
    attribute_list = [i[0] for i in cursor.description]
    insert_command = f"INSERT INTO {table} ("
    uid = input("Please enter the 3 digit ID of the item you would like to enter into the database:\n")
    #adds all columns to insert statement
    for i in range(0, num_attributes-1):
        insert_command += f"{attribute_list[i]}, "
    insert_command += f"{attribute_list[num_attributes-1]})"
    insert_command += f" VALUES ({uid}, "
    
    #adds each data entry to insert statement
    for i in range(1, num_attributes-1):
        data = input(f"Enter the info you would like to enter into the '{attribute_list[i]}' column:\n")
        insert_command += f"'{data}', "
    data = input(f"Enter the info you would like to enter into the '{attribute_list[num_attributes-1]}' column:\n")
    insert_command += f"'{data}')"

    #Try to execute statement, print error message if fails
    print(f"Attempting to execute command:\n {insert_command}")
    try:
        cursor.execute(insert_command)
        print("Insertion Executed Succesfully")
    except Exception as e:
        print("Error With Data")
        print(e)

    
    


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
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            attributes = cursor.column_names

            file.close()
            valid = True

        except Exception as e:
            print("Error Opening File: ", e)

#         atr_str = ' , '.join(attributes)
#         value_str = ' , '.join(['%s' for i in range(len(df.columns))])

#         cursor.execute(f"""
#         INSERT INTO {table_name} ({atr_str})
#         VALUES
# (001, "Benedetto da Rovezzano", "1474", "1554"),""")

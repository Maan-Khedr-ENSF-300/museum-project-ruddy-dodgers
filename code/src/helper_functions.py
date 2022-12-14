from tabulate import tabulate


def print_table(cursor):
    """Prints out the resulting table from a query in a formatted way
    Args:
        cursor: cursor object that can used to execute queries and fetch results 
        for the chosen database
    """

    rows = cursor.fetchall()

    print("Table Looks like: ")
    print(tabulate(rows, headers=cursor.column_names, tablefmt="grid"))


def choose_table(cursor):

    cursor.execute("SHOW TABLES;")
    print_table(cursor)

    while True:
        try:
            table = input("What table you like to use: ")
            cursor.execute(f"SELECT * FROM {table}")
            return table
        except Exception as e:
            print(e)
            print("Error Fetching Table")
            break

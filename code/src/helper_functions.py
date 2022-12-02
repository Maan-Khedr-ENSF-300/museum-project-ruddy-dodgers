from tabulate import tabulate


def print_table(cursor):
    """Prints out the resulting table from a query in a formatted way
    Args:
        cursor: cursor object that can used to execute queries and fetch results 
        for the chosen database
    """
    rows = cursor.fetchall()

    print("\nQuery Executed Successfully!")
    print("Table Looks like: ")
    print(tabulate(rows, headers=cursor.column_names, tablefmt="grid"))

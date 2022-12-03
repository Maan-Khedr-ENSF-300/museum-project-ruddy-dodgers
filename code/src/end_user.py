from helper_functions import *


def browsing_main_menu(cursor):

    chosen = False
    while not chosen:
        choice = input(
            "What would you like to browse:\n1. Art Pieces\n2. Exhibitions\n3. Artists\n4. Collections\n0. Quit\n9. Logout")

        if choice == '1':
            art_menu()

        elif choice == '2':
            exhibition_menu(cursor)

        elif choice == '3':
            artist_menu(cursor)

        elif choice == '4':
            collection_menu(cursor)

        elif choice == '0':
            chosen = True
            return False

        elif choice == '9':
            chosen = True
            print('Logging Out!')
            return True

        else:
            print("Invalid Input. Please try again.")


def exhibition_menu(cursor):
    pass


def artist_menu(cursor):
    iteration = 0
    browsing = True
    while browsing:
        if iteration != 0:
            browsing = continue_browsing()

        try:
            cursor.execute("SELECT NAME FROM ARTIST")
            print_table(cursor)
            collection_name = input(
                "Please enter the name of the Artist you would like to browse: ")

            cursor.execute(
                f"SELECT * FROM ARTIST WHERE NAME = '{collection_name}'")
            print_table(cursor)

        except Exception as e:
            print("\nThere was an error, please try again")
            print(e)

        iteration += 1


def collection_menu(cursor):
    # TODO - CHANGE WHAT DATA IS DISPLAYED?

    iteration = 0
    browsing = True
    while browsing:
        if iteration != 0:
            browsing = continue_browsing()

        try:
            cursor.execute("SELECT NAME FROM COLLECTION")
            print_table(cursor)
            collection_name = input(
                "Please enter the name of the collection you would like to browse: ")

            cursor.execute(
                f"SELECT * FROM COLLECTION WHERE NAME = '{collection_name}'")
            print_table(cursor)

        except Exception as e:
            print("\nThere was an error, please try again")
            print(e)

        iteration += 1


def art_menu(cursor):
    # TODO - Provide information on whether the art_object is part of a permanent collection or it is borrowed
    # TODO - Provide information on the artist and background of the art_object (potentially create a custom print statement)

    iteration = 0
    browsing = True
    while browsing:
        if iteration != 0:
            browsing = continue_browsing()

        try:
            choice = input(
                "What type of Art Pieces would you like to browse:\n1. Paintings\n2.Sculptures/Statues\n3.Other\n0.Back")

            if choice == "1":
                cursor.execute(
                    "SELECT * FROM PAINTING AS P, ART_OBJECT AS A WHERE A.unique_id = P.unique_id")
                print_table(cursor)

            elif choice == "2":
                cursor.execute(
                    "SELECT * FROM SCULPTURE_STATUE AS S, ART_OBJECT AS A WHERE A.unique_id = S.unique_id")
                print_table(cursor)

            elif choice == "3":
                cursor.execute(
                    "SELECT * FROM OTHER AS O, ART_OBJECT AS A WHERE A.unique_id = O.unique_id")
                print_table(cursor)

            elif choice == "0":
                return

            else:
                print("Invalid Input. Please try again.")

        except Exception as e:
            print("\nThere was an error, please try again")
            print(e)

        iteration += 1


def continue_browsing():

    while True:
        option = input(
            "Would you like to continue browsing (1) or do you want to go back to the main menu (2): ")

        if option == '1':
            return True

        elif option == '2':
            return False

        else:
            print("Invalid Input. Please try again.")

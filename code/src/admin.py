def init_database(cursor):
    fd = open('DBinit.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except Exception as e:
            print("Command skipped: ", e)


def add_user():
    pass


def edit_user():
    pass

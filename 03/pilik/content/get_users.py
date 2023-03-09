import sqlite3
try:
    sqliteConnection = sqlite3.connect('./db/SQLite_Python.db')
    sqlite_create_table_query = '''select * from user;'''

    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    records = cursor.fetchall()
    for row in records:
        print('id: {}'.format(row[0]))
        print('name: {}'.format(row[1]))

    cursor.close()

except sqlite3.Error as error:
    print("Error while querying a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
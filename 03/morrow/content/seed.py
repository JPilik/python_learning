import sqlite3
try:
    sqliteConnection = sqlite3.connect('./db/SQLite_Python.db')
    sqlite_create_table_querys = [
    '''CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
        );
    '''
    , 
    '''
        CREATE TABLE IF NOT EXISTS character (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
        );'''
    ,
    '''
        CREATE TABLE IF NOT EXISTS user_character (
        userid INTEGER,
        characterid INTEGER
        );'''
    ,
    '''
        CREATE TABLE IF NOT EXISTS weapon (
        id INTEGER PRIMARY KEY,
        name  TEXT NOT NULL
        );'''
    ,
    '''
        CREATE TABLE IF NOT EXISTS character_weapon (
        characterid INTEGER,
        weaponid INTEGER
        );'''
    ,
        ''' 
        CREATE TABLE IF NOT EXISTS spell (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
        );'''
    ,
    '''
        CREATE TABLE IF NOT EXISTS character_spell (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
        );'''
    ,
        '''                          
        CREATE TABLE IF NOT EXISTS user_event (
        id INTEGER PRIMARY KEY,
        userid INTEGER NOT NULL,
        record TEXT NOT NULL
        );
        ''',
        '''INSERT INTO weapon (name) values ('axe'), ('sword'), ('dagger'), ('crossbow'), ('short bow'), ('long bow'), ('pike'), ('fists');''',
        '''INSERT INTO spell (name) values ('fireball'), ('lightning'), ('warp'), ('magic missles'), ('heal'), ('burn'), ('charm'), ('disintegrate');''',
        '''INSERT INTO user (name) values ('bill'), ('bob'), ('butters'), ('pee wee'), ('george');''',
        '''INSERT INTO character (name) values ('analie'),('raiden'), ('serkan'), ('arcelia'), ('avyanna'), ('torren'), ('hollis'), ('bellamy'), ('llyrana'), ('mirk'), ('aenna')''',
    ]
    
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    for query in sqlite_create_table_querys:
        print(query)
        cursor.execute(query)
        sqliteConnection.commit()
        print("SQLite table prepared")

    cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")
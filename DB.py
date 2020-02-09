import sqlite3


def create_table_users(name_table):
    conn_db = sqlite3.connect(name_table)
    cursor = conn_db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL, 
        email TEXT NOT NULL UNIQUE
        )
        ''')
    conn_db.close()


create_table_users('test_db.sqlite')
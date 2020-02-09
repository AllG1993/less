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


def add_user(name_table):
    conn_db = sqlite3.connect(name_table)
    cursor = conn_db.cursor()
    cursor.execute('''
    INSERT INTO users
    (name, email)
    VALUES ("Petrov Petr", "petrov@gmail.com")''')
    conn_db.commit()
    conn_db.close()


users = [
    ('Анатолий Шишков', 'tolikebolik@gmail.com'),
    ('Василий Иванов', 'vasyaivanov@gmail.com'),
    ('Григорий Мединский', 'medy@gmail.com'),
    ('Владимир Борисов', 'borisov@gmail.com'),
    ('Екатерина Исакова', 'isakova@gmail.com'),
    ('Анастасия Володина', 'nagibatormamok@gmail.com'),
    ('Киркоров Филипп', 'fi@gmail.com'),
    ('Надежда Кадышева', 'nadikad@gmail.com'),
    ('Альберт Энштейн', 'vseotnositelno@gmail.com')
]


def add_many_user(name_table):
    conn_db = sqlite3.connect(name_table)
    cursor = conn_db.cursor()
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
    conn_db.commit()
    conn_db.close()


def get_data(name_table, email):
    conn_db = sqlite3.connect(name_table)
    cursor = conn_db.cursor()

    cursor.execute("SELECT * FROM users")

    data = cursor.fetchall()

    for users in data:
        print(users[0], users[1], users[2])

    conn_db.close()


get_data('test_db.sqlite', 'nadikad@gmail.com')
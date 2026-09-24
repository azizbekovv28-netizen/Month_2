#SQL =  structured query language
#data = данные
#SQLite, PostreSQL, MySQL, MSSQL
import sqlite3

def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

def add_student(conn, name, age, city):
    print(name, age, city)
    conn.execute("""
    INSERT INTO students 
    VALUES (?, ?, ?)
    """,
    (name, age, city)
    )
    conn.commit()

if __name__ == '__main__':
    connection = sqlite3.connect('database.db')
    create_table(connection)
    add_student(connection, 'Azim', 22, 'Bishkek')
    add_student(connection, 'Daniyar', 36, 'Naryn')

    connection.close()
import sqlite3

def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
        name TEXT, 
        author TEXT, 
        publication_year INTEGER, 
        genre TEXT, 
        number_of_pages INTEGER, 
        number_of_copies INTEGER
        )
    """)

def insert_books(conn, name, author, publication_year, genre,
                   number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books 
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, publication_year, genre,
          number_of_pages, number_of_copies)
    )
    conn.commit()

if __name__ == "__main__":
    connection = sqlite3.connect("database_books.db")
    create_table(connection)

    insert_books(connection, "Преступление и наказание",
                   "Федор Достоевский",
                   1866,
                   "Роман",
                480,
                   5)

    insert_books(connection, "1984",
                   "Джордж Оруэлл",
                   1949,
                   "Антиутопия",
                   320,
                   4)

    insert_books(connection, "Маленький принц",
                   "Антуан де Сент-Экзюпери",
                   1943,
                   "Сказка",
                   96,
                   8)

    insert_books(connection, "Война и мир",
                   "Лев Толстой",
                   1869,
                   "Роман",
                   224,
                   6)

    insert_books(connection, "Мастер и Маргарита",
                   "Михаил Булгаков",
                   1967,
                   "Роман",
                   480,
                   5)

    insert_books(connection, "Герой нашего времени",
                   "Михаил Лермонтов",
                   1840,
                   "Роман",
                   224,
                   6)

    insert_books(connection, "Вино из одуванчиков",
                   "Рэй Брэдбери",
                   1957,
                   "Фантастика",
                   320,
                   4)

    insert_books(connection, "Гарри Поттер и философский камень",
                   "Джоан Роулинг",
                   1997,
                   "Фэнтези",
                   399,
                   10)

    insert_books(connection, "Собачье сердце",
                   "Михаил Булгаков",
                   1925,
                   "Сатира",
                   128,
                   7)

    insert_books(connection, "Три товарища",
                   "Эрих Мария Ремарк",
                   1936,
                   "Роман",
                   480,
                   3)
    connection.close()
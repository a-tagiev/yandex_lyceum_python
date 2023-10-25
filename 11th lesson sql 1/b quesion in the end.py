import sqlite3

db_filename = input()

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
get_genre = """
    SELECT title
    FROM films
    WHERE title LIKE '%?'
    """
results = cursor.execute(get_genre).fetchall()
for row in results:
    print(row[0])

conn.close()

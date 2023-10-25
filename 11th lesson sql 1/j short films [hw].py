import sqlite3

db_filename = input()

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
get_genre = """
    SELECT title
    FROM films
    WHERE duration<=85
    """
arr = cursor.execute(get_genre).fetchall()
for row in arr:
    print(row[0])

conn.close()

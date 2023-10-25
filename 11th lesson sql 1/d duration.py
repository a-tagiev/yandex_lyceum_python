import sqlite3

db_filename = input()

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
get_genre = """
    SELECT id
    FROM genres
    WHERE title = 'комедия';
    """
arr = cursor.execute(get_genre).fetchall()

q = f"""
    SELECT title
    FROM films
    WHERE (duration>=60 AND genre={arr[0][0]});
    """
results = cursor.execute(q).fetchall()
for row in results:
    print(row[0])

conn.close()

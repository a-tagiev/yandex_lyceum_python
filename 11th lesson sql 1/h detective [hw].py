import sqlite3

db_filename = input()

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
get_genre = """
    SELECT id
    FROM genres
    WHERE title = 'детектив';
    """
arr = cursor.execute(get_genre).fetchall()
print(arr[0][0])
query = f"SELECT title FROM films WHERE (genre = {arr[0][0]} AND year BETWEEN 1995 AND 2000)"
results = cursor.execute(query).fetchall()
for row in results:
    print(row[0])

conn.close()

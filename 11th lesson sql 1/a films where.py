import sqlite3

db_filename = input()

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
get_genre = """
    SELECT id
    FROM genres
    WHERE title = 'музыка' OR title = 'анимация'
    """
arr = cursor.execute(get_genre).fetchall()

query = f'SELECT title FROM films WHERE (genre = {arr[0][0]} OR genre ={arr[1][0]} ) AND year >= 1997'
results = cursor.execute(query).fetchall()
for row in results:
    print(row[0])

conn.close()

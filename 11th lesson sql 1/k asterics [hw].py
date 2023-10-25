import sqlite3

db_filename = input()

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
get = """
SELECT title
FROM films
WHERE title LIKE '%Астерикс%'
AND title NOT LIKE '%Обеликс%';
    """
arr = cursor.execute(get).fetchall()
for row in arr:
    print(row[0])

conn.close()

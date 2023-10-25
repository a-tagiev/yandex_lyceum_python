import sqlite3

db_filename = input()

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
get_genre_numb = """
    SELECT DISTINCT genre
    FROM films
    WHERE year IN (2010, 2011)
    """
results = cursor.execute(get_genre_numb).fetchall()
ans = []
for row in results:
    q = f"""SELECT title FROM genres WHERE id ={row[0]}"""
    ans.append(cursor.execute(q).fetchall())
for i in ans:
    print(*i[0])
conn.close()

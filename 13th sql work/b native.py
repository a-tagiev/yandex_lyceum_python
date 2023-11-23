import sqlite3

inp = list(input())
conn = sqlite3.connect("native.db")
cursor = conn.cursor()

inp_tuple = tuple(map(str, inp))

get_pl = """
    SELECT place
    FROM Places
    WHERE location IN ({})
    ORDER BY how_far DESC
    """.format(', '.join(['?'] * len(inp)))

arr = cursor.execute(get_pl, inp_tuple).fetchall()
for place in arr:
    print(place[0])

conn.close()

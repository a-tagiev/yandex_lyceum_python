import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    get_genre = """
        SELECT id
        FROM genres
        WHERE title = 'фантастика';
        """
    genre = cursor.execute(get_genre).fetchone()[0]
    change_duration = f"""
        UPDATE films
SET duration = duration*2
WHERE genre={genre};
        """
    cursor.execute(change_duration).fetchall()
    conn.commit()
    conn.close()


get_result("films_db.sqlite")

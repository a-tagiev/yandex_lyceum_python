import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    get_genre = """
        SELECT id
        FROM genres
        WHERE title = 'боевик';
        """
    genre = cursor.execute(get_genre).fetchone()[0]
    delete_films = f"""
        DELETE FROM films
WHERE genre={genre} AND duration>=90;
        """
    cursor.execute(delete_films).fetchall()
    conn.commit()
    conn.close()

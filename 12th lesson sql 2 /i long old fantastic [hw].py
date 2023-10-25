import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    get_genre = """
        SELECT id
        FROM genres
        WHERE title = 'фантастика'
        """
    genre = cursor.execute(get_genre).fetchone()[0]
    delete_from_table = f"""
        DELETE FROM films WHERE year<2000 AND duration>90 and genre={genre}
        """
    cursor.execute(delete_from_table).fetchall()
    conn.commit()
    conn.close()

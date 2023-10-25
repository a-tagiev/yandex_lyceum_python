import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    get_genre = """
        SELECT id
        FROM genres
        WHERE title = 'мюзикл';
        """
    genre = cursor.execute(get_genre).fetchone()[0]
    delete_films = f"""
        UPDATE films
        SET duration = 100
WHERE duration>100 AND genre={genre};
        """
    cursor.execute(delete_films).fetchall()
    conn.commit()
    conn.close()

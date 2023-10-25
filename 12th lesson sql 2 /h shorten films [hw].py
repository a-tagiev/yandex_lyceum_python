import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    delete_films = f"""
        UPDATE films
        SET duration = duration/3
WHERE year=1973;
        """
    cursor.execute(delete_films).fetchall()
    conn.commit()
    conn.close()

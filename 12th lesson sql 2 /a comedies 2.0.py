import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    get_comedy_id = """
        SELECT id
        FROM genres
        WHERE title = 'комедия';
        """
    result = cursor.execute(get_comedy_id).fetchone()[0]
    delete_from_table = f"""
        DELETE FROM films WHERE genre = '{result}'
        """
    cursor.execute(delete_from_table).fetchall()
    conn.commit()
    conn.close()

import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    delete_from_table = f"""
        DELETE FROM films WHERE title LIKE 'Я%а'
        """
    cursor.execute(delete_from_table).fetchall()
    conn.commit()
    conn.close()

import sqlite3


def get_result(name):
    conn = sqlite3.connect(name)
    cursor = conn.cursor()
    change_duration = f"""
        UPDATE films
SET duration = '42'
WHERE duration='';
        """
    cursor.execute(change_duration).fetchall()
    conn.commit()
    conn.close()


get_result("films_db.sqlite")

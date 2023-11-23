import sqlite3


def arrival(*data, sort=False):
    conn = sqlite3.connect("duties.db")
    cursor = conn.cursor()

    cities_str = ', '.join(['?'] * len(data))

    query = f"""
        SELECT p.name, f.fee * c.ratio
        FROM People p
        JOIN Cities c ON p.city_id = c.id
        JOIN Fees f ON p.reason_id = f.id
        WHERE c.city IN ({cities_str})
    """

    if sort:
        query += "ORDER BY f.fee * c.ratio DESC, p.name"
    else:
        query += "ORDER BY f.fee * c.ratio, p.name"

    result = cursor.execute(query, data).fetchall()

    conn.close()
    return result

#!/usr/bin/python3
"""List all cities of a state."""

if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = sys.argv

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )

    cur = conn.cursor()

    query = f"""
        SELECT name
        FROM cities
        WHERE cities.state_id = (
            SELECT id
            FROM states
            WHERE name = '{argv[4]}'
        )
    """

    cur.execute(query)

    rows = cur.fetchall()
    rows_to_pure_list = [item[0] for item in rows]

    print(", ".join(rows_to_pure_list))

    cur.close()
    conn.close()

#!/usr/bin/python3
"""
List all states with a name starting with uppercase N
from database hbtn_0e_0_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    argv = sys.argv

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()

    query = """
        SELECT *
        FROM {}.states
        WHERE BINARY SUBSTRING(name, 1, 1)='N'
        ORDER BY states.id ASC
    """.format(argv[3])

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

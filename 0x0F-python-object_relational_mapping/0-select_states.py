#!/usr/bin/python3
""" A module that lists al states from a database."""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(f"SELECT * FROM {sys.argv[3]}.states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

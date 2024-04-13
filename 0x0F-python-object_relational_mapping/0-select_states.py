#!/usr/bin/python3
""" A module that lists al states from a database."""

if __name__ == '__main__':
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
    cur.execute(f"SELECT * FROM {argv[3]}.states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

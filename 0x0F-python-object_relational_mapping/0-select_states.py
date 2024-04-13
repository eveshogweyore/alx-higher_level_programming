#!/usr/bin/python3
""" A module that lists al states from a database."""

if __name__ == '__main__':
    import MySQLdb as sql
    import sys

    argv = sys.argv

    db = sql.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

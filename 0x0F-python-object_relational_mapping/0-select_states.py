#!/usr/bin/python3
""" A module that lists al states from a database."""

if __name__ == '__main__':
    import MySQLdb as sql
    import sys

    argv = sys.argv

    db = sql.connect(
        host=argv[1],
        user=argv[2],
        passwd='',
        db=argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()

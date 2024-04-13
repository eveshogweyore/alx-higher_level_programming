#!/usr/bin/python3
"""
Displays all values in `states` table where name matches argument
"""

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

    name = argv[4]
    query = """
        SELECT *
        FROM {}.states
        WHERE name='{}'
        ORDER BY states.id ASC
    """.format(argv[3], name)

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

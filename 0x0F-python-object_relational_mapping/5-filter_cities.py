#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT cities.name FROM cities
        JOIN states
        On states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY cities.id ASC""",
        (argv[4],),
    )
    query_rows = cur.fetchall()
    str = ', '.join(map(lambda x: x[0], query_rows))
    print(str)

    cur.close()
    conn.close()

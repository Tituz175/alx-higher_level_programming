#!/usr/bin/python3
"""
This module is a python script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
provided via the command line
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_state = sys.argv[4]

    db = MySQLdb.connect(
        host=host, port=3306, user=user, password=password, db=database,
        charset="utf8"
        )

    query = "SELECT * FROM states WHERE name LIKE BINARY  %s ORDER BY id"

    cursor = db.cursor()
    cursor.execute(query, (search_state, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

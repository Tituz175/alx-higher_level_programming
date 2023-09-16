#!/usr/bin/python3
"""This python script is used to print all the states in the database."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    host = "localhost"
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host=host, port=3306, user=user, password=password, db=database
        )

    query = "SELECT * FROM states ORDER BY id"

    cursor = db.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

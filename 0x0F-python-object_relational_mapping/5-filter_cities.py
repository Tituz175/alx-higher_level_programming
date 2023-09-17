#!/usr/bin/python3
"""
This script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    host = 'localhost'
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host=host, port=3306, user=user, password=password, db=database
        )

    query = """SELECT * """\
        """FROM cities INNER JOIN states ON cities.state_id = states.id """\
        """ORDER BY cities.id"""

    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(", ".join([row[2] for row in results if row[-1] == state_name]))
    cursor.close()
    db.close()

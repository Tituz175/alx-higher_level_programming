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

    query = """SELECT cities.id, cities.name, states.name """\
        """FROM cities JOIN states ON cities.state_id = states.id """\
        """WHERE states.name = '{}'"""\
        """ORDER BY cities.id""".format(state_name)

    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        if results.index(row) == len(results) - 1:
            print(row[-2])
        else:
            print(row[-2], end=", ")

    cursor.close()
    db.close()

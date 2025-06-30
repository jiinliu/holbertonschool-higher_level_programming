#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
    ists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username, password, db_name, state_name_searched = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        )
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities JOIN ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC",
        (state_name_searched,)
        )

    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    # Cleanup
    cursor.close()
    db.close()

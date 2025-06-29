#!/usr/bin/python3
""" takes in an argument and displays all values in the states table 
    of hbtn_0e_0_usa where name matches the argument,
    that is safe from MySQL injections.
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
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (state_name_searched,)
        )

    for row in cursor.fetchall():
        print(row)

    # Cleanup
    cursor.close()
    db.close()

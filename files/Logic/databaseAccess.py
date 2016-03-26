#!/usr/bin/python

import pymysql


def openDatabase(tablequery):
    # Open database connection
    table = tablequery
    return pymysql.connect(host="jdbc:mysql://mysql.cs.iastate.edu", user="dbu309grp17", passwd="AugtUmP22JP", db=table)



# prepare a cursor object using cursor() method
# cursor = db.cursor()

# execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
# data = cursor.fetchone()

# disconnect from server
# db.close()

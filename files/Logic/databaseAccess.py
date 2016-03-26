#!/usr/bin/python

import pymysql

def openDatabase(tablequery):
# Open database connection
db=pymysql.connect(host="jdbc:mysql://mysql.cs.iastate.edu",user="dbu309grp17", passwd="AugtUmP22JP",db=tablequery)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()
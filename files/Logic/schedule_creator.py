#
#This is the code in which the schedules will be generated with.
#
#!/usr/bin/python


import pymysql

db=pymysql.connect(host="jdbc:mysql://mysql.cs.iastate.edu",user="dbu309grp17",
                  passwd="AugtUmP22JP",db="thangs")


class ScheduleCreator:

TODO
#Function
##Write a function that connects to the Database
#return connection
def databaseConnection():

TODO
#Function
##Write a function that queries database
#return the query
def databaseQuery():

TODO
#Function
##Write a function that takes in 2 arguments
###1. list of required classes
###2. list of classes already taken
##filter through removing classes which appear in both arrays/lists (type tbd)
#return list of filtered classes
def classFilter():

TODO
#Function
##Write a function that checks pre-requisites
def prereq():


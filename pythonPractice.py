import pymysql

# This file is for python practice and is not to be used in the actual project

# Function that return a passed string


# print a statement to console
def printlife(passedString):
    print(passedString)
    return

printlife("hello world!")
printlife("life is good")
printlife("Samsung")

# return a variable then use it (print)
def returnVar():
    variable = 123456789
    return variable

temp = returnVar()
print(temp)

print()

#TODO
# does not work as of right now
# Function which will query the database
def openDatabase(tablequery):
    # Open database connection
    print(tablequery)
    table = tablequery
    print(table)
    pymysql.connect(host="mysql.cs.iastate.edu", user="dbu309grp17", passwd="AugtUmP22JP", db=tablequery)

openDatabase("auth_group")

# Functions
def hello(name):
    print("Hello" + name)
    return 0
hello("world!")
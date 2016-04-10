# Examples

myNumber = 3
strNum = str(myNumber)
string = "Hello World"
#Lists
nums=[]
num.append(21)
#Dictionaries (Table of Values and Keys)
dictionary={'key': 'value'}

#printing
name = "Annie"
print("Hello, " + name)
print("Hello, ", name)

name = input("Enter name: ")

if x < 2:
	x = 0
elif x == 2:
else:
	x = 1

#Functions
def hello(name):
	print("Hello" + name)
	return 0

hello()

#Using Main
def Main():
	print("Main")

#Tells python you want to use the main funciton
if ___name__ == "__main__":
	Main()

#for loop
#Counts up to 5 not including 5
for step in range(5):

#For in
words = ['hi', 'no']
for word in words:
	print(word)

#While Loop
while num < 1:
	num = int(input("Enter number: "))

while True:
	print("is true")

#File IO
#r for read mode
#w for write mode
f = open("myFile.txt", "r") 
for line in f:
	#Strip takes off new line characters
	print(line.strip("\n\r"))
f.write(input("Code to write to file: ") + "\n")
f.close()
#With loops
words = {"cat", "sat"}
with open("words.txt", "w") as f:
	for word in words:
		f.write(word + "\n")

#Exceptions
try:
	print("try this stuff")
except:
	print("Do this stuff when it fails")
finally:
	print("always do this")

#Modules
import math
math.fabs(1)

#Classes
class MyClass:
	number = 0
	name = "name"
	#Constructor
	def __init__(self, number, name):
		self.number = number
		self.name = name

def useClass():
	me = MyClass()
	me.number = 0

#Inheritance
class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class Cat(Pet):
	def __init__(self, name, age):
		#Calling super class methods
		super().__init__(name, age)
#Initializing Objects
thePet = Pet("Pet", 1)
#Returns boolean
isinstance(thePet, Pet)

#Modulating Code
import vector2d
vec1 = vector2d.Vector2D(5, 6)

from vector2d import Vector2D #alternatively a * for everything
vec1 = Vector2D(5, 6)

#Templates
from string import Template

def Main():
	cart = []
	cart.append(dict(item="Coke", price=8, qty=2))
	t = Template("qty x $item = $price")
	print(t.safe_substitue(cart[0]))

#Argparse
import argparse

parser = argparse.ArugmentParser()
#Muterally exclusive group
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="store_true")
if arg.verbose:
	print("verbose argument is set")

group.add_argument("-q", "--quiet", action="store_true")
if args.quiet:
	print("quit argument is set")
parser.add_argument("num", help="Num Entered: ", type=int)
parser.add_argument("-o", "--output", help="Output result to a file", 
	action="store_true")
args = parser.parse_args()
result = args.num











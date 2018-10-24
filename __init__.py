#!/usr/bin/python
#general stuff

#tutorials
#1
#https://docs.python.org/3/tutorial/classes.html
#https://www.learnpython.org/en/Variables_and_Types
#https://docs.python.org/3/reference/simple_stmts.html#the-del-statement
#2
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#3
#https://www.tutorialspoint.com/python/python_basic_syntax.htm

import random
import ACl

print("\n")

bcl = ACl.ACl()
bcl.print()
bcl.value = 7
ACl.acl.print()
ACl.acl.value = 9
bcl.print()
ACl.acl.print()

del bcl.value
bcl.print()

def add(x,  y):
    return x+ y * 2

print("\nAdd(2, 3) = ",  add(2,  3))

print("Hello, World!")
x = 1 + random.random()
print(" rand x = ",  x)
y = True
z = False
if y and (z or x):
    print("True!")
else:
    print("False!")
    x = 7
    
#read file
print("x = ",  x)
file = open("test.txt",  "r")
print(file)
c = 0
for line in file:
    print(line)
    c += 1

d = 0
while d != 10:
    d += 1

print("d = ",  d)

print("line counter",  c)
file.close()

#write file
file2 = open("test2.txt",  "r")
file2.write("Line 1\n")
d = "2"
file2.write("Line " +  "___" + d + "\n")
file2.write("Line 3\n")

file2.close()

#language
for xc in range(1, 8, 1):
    print("xc = ",  xc)

#file tricks
with open("test3.txt",  "r") as file3:
    print(file3.read())
    
for key in {'one':3, 'two':7}:
    print(key)
    
y = 3
#with y as x:
#    print("x = ",  x)


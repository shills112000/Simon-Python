# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:58:58 2018

@author: SHills
"""

# add to the list

mystring = "hello"

mylist = []

for letter in mystring:
    mylist.append(letter)
    
print (mylist)

# same thing as above

mylist = []
mylist = [letter for letter in mystring]
print (mylist)

mylist = [x for x in range(0,11)]
print (mylist)

# same as above but square the x
mylist = [x**2 for x in range(0,11)]
print (mylist)

mylist = [x for x in range(0,11) if x%2==0]
print (mylist)

celcius= [0,10,20,34.5]

far=[((9/5)*temp + 32) for temp in celcius]
print (far)

mylist=[]

for x in [2,4,6]:
    for y in [200,300]:
        mylist.append(x*y)

print (mylist)
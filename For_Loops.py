# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 15:26:13 2018

@author: Simon
"""

# Iterable  means you can iterate over the object ... perform a action for everything in a object

my_list = [1,2,3]
for entry in my_list:
    print (entry)


my_list =[1,2,3,4,5,6,7,8,9,10]

for entry in my_list:
    if entry == 1:
        print (entry)
    elif entry % 2 == 0:   # print only even numbers
        print (f'Even number :{entry}')
    else:
        print (f'Odd number : {entry}')

list_sum = 0
for num in my_list:
    list_sum = list_sum + num
    
print (f'All numbers added up is : {list_sum}')


mystring = 'Hello World'

for letter in mystring:
    print (letter)
    
for _ in mystring:    # The _ means iterate through the whole string
    print ("I'm cool")
    
    
tup = (1,2,3)  # remember tuples are immutable ie cannot be changed, that is how they differ from lists
for item in tup:
    print (item)
    
# Now have a list with tuples in it
    
my_list = [(1,2),(3,4),(5,6)]

for entry in my_list:
    print (entry)
    
for (a,b) in my_list:  # tuple upacking
    print (a)
    print (b)
    
my_list=[(1,2,3),(5,6,7),(7,8,9)]

for a,b,c in my_list:
    print (b)
    
d = {'k1':1,'k2':2,'k3':3}

for item in d:   # notice only iterate trhough keys
    print (item)
    
for item in d.items():   # notice iterate  keys and values
    print (item)
    
for key,value in d.items():  # just show values
    print (value)
    

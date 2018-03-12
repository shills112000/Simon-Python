# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:55:45 2018

@author: SHills
"""

# range function

for num in range(10):  # will print all numbers up to 10
    print (num)
    
for num in range(3,10):  # will print all numbers from 3 up to 10
    print (num)
    
for num in range(0,10,2):  # will print all numbers from 3 up to 10 steping 2
    print (num)

index_count=0
for letter in  'abcde' :
    print ('At index {} the letter is {}' .format(index_count,letter))
    index_count +=1
    
# The above code can be done like
    
index_count=0
word= 'abcde'
for letter in  word :
    print (word[index_count])
    index_count +=1   
 
    
# enumerate function
word= 'abcde'
for item in  enumerate(word) :
    print (item)
    
word= 'abcde'
for index,letter in enumerate(word) :
    print (index)
    print (letter)
    print ('\n')

# zip function (opposite of enumerate), only zips as far as least elements in list
mylist1 =[1,2,3,4,5,6,7]
mylist2 =['a','b','c','d','e']
mylist3 =[100,200,300,400,500]

for item in zip(mylist1,mylist2,mylist3):
    print(item)

for a,b,c in zip(mylist1,mylist2,mylist3):  # just how the mylist1 entrys
    print(a)

# Check if some exists using in operator
'x' in [1,2,3]   # is x in this list gives boolean
2 in [1,2,3]
'a' in 'a world'

'mykey' in {'mykey':345}

d = {'mykey':345}
345 in d.keys()
345 in d.values()
'mykey' in d.keys()


mylist =[10,20,30,40,50]
x = min(mylist)  # get min number in list
print (x)
y = max(mylist) # get max number in list
print (y)

# random library
from random import shuffle    # import from random the shuffle function
mylist= [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)

# get random interger
from random import randint

y = randint(0,100)
print (y)

result = input ('enter a number: ')

print (f'Hi number is {result}')
type(result)

# turn input into a float number
float(result)
type(result)
x = int(result)
type (x)



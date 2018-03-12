# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:36:41 2018

@author: SHills
"""

x = 0
while x < 5:
    print (f' The current value of x is {x}')
    x = x + 1
   # x +=1   # nice way of writing x=x+1
else:
    print ("X is not less than 5")

# break  - break out of the current closed enclosing loop
# continue - goes to the top of hte closet enclosing loop
# pass: does nothing at all

x=[1,2,3]
for item in x:
    # comment
    pass # do nothing at all , eg placholder script
    
mystring = "Sammy"

for letter in mystring:
    if letter == 'a':   # if letter is a then miss it
        continue
    print (letter)
    

    mystring = "Sammy"

for letter in mystring:
    if letter == 'a':   # if letter is a break out of loop
        break
    print (letter)

x = 0 
while x < 5:
    if x == 2:
        break   # break out while loop if x is equal to 2
    print (x)
    x +=1

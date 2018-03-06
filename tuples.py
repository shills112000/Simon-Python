# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:44:03 2018

@author: Simon
"""

#tuples are immutable, ie they cannot be changed

t=(1,2,3) # tuple
my_list=[1,2,3] # list
type(t)
type(my_list)
len(t)
t=('one',2)
t[0]
t=('a','a','a','b')
t.count('a') # counts how many a's are in the list
t.index('a') # shows where the first a element is which is 0
t.index('b') # shows where the first a element is which is 3
my_list[0]='NEW'
t[0]='NEW'  # This will fail as tuples cannot be changed.

#TUPLES Are used for data intergrity 


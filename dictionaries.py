# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 14:11:11 2018

@author: Simon
"""

my_dict = {'key1':'value1','key2':'value2'}
# dictionaries cannot be sorted or sliced or indexed like lists
my_dict['key1'] # get value of key1

prices_lookup = {'apple':2.99,'pear':3.99}
prices_lookup['apple']

d= {'k1':123,'k2':[0,1,2],'k3':{'insideley':100}}
# dictionaries can hold lists or other dictionaires
d['k2'][2] # key2 at telment 2  is 2

d= {'key1':['a','b','c']}   # example set dictionary to have a list
my_list=d['key1'] # my_list = key1
letter=my_list[2] # letter has last element
letter.upper() # uppercase letter

d['key1'][2].upper() # same as above, but all in one step

d={'k1':100,'k2':200}
d['k3']=300
d['k1']=500

d={'k1':100,'k2':200}
d.keys()  # get all keys in dictionary
d.values() # get all values in dictionary
d.items()  # get all the pairs together
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 15:13:30 2018

@author: Simon
"""

# basic file input ouput

myfile=open('TEST.txt')
# myfile=open('NOTHERE_FILE.txt') #  check file exists get whoops if fails

myfile.read()  # gets giant string

myfile.read()  # if you read again the cursour is now at the end of the file
myfile.seek(0) # go back to top of file
myfile.read() # now you can read again
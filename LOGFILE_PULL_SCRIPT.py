# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:08:31 2018

@author: SHills
"""
#!/usr/bin/env python

env_name=[]
env_jboss=[]
file = open ('ENVS',"r")
for line in file:
        fields=line.split(",")
        env_name.append(fields[0])
        env_jboss.append(fields[1])

print ("Please choose the number below for the enviroment you wish to collect the log files from :\n")
x=0
type (x)
for entry in env_name:
        print ("{0}. {1} " .format(x+1,env_name[x]))
        x+=1

length=len(env_name)
result = input ('enter a number: ')
while result < 1 or result > length:
        print ("Number needs to be inbetween 1 and {0}" .format(length))
        result = input ('enter a number: ')

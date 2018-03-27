# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:08:31 2018

@author: SHills
"""
#!/usr/bin/env python

import sys, os

env_name=[]
env_jboss=[]
file = open ('ENVS',"r")
for line in file:
        fields=line.split(",")
        env_name.append(fields[0])
        env_jboss.append(fields[1])

print ("Please choose the number below for the enviroment you wish to collect the log files from :\n")
x=0
for entry in env_name:
        print ("{0}. {1} " .format(x+1,env_name[x]))
        x+=1

length=len(env_name)
result = input ('enter a number: ')
while result < 1 or result > length:
        print ("Number needs to be inbetween 1 and {0}" .format(length))
        result = input ('enter a number: ')

enviroment=env_name[result-1]
hostname=env_jboss[result-1]

print (result)
print ("You Choose: {0} and the server is {1}" .format(enviroment, hostname))


# rstrip is like perl chomp
hostname=hostname.rstrip("\n")

cmd = "ssh " + hostname + " date"
os.system(cmd)

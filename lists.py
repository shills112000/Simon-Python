# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:49:13 2018

@author: SHills
"""
my_list=[1,2,3]
my_list=['string',1,2,3]
len(my_list) 
mylist= ['one','two','three']
mylist[1:] # indexing 
another_list=['four','five']
new_list= mylist + another_list
print (f'{new_list}')

new_list[0]='One all caps' # change element in list
new_list.append('six') # add to the end of the list
new_list.pop()  # removes last entry
pop_item=new_list.pop() # save last item to pop_item
pop_item=new_list.pop(1) # remove 2nd entry in list
new_list = ['a','e','x','b','c']
num_list =[4,1,8,3]
new_list.sort()  # sprts new_list , it changes the list
num_list.sort() # sorts numbers
num_list.reverse() # reverses a list
simon
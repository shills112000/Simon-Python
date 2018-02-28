print ('hello world1')
mystring="Hello world"
mystring[2] # imdex 0 , starts at 0 
mystring[2:] # : to end of string
mystring[:3]  # got upto 3rd letter
mystring[3:6] # l to w
mystring[::-1]  # reserves the string  
last_letters=mystring[1:]
'P' + last_letters
x="Hello World"
x= x + " it is beautful outside"
x.upper()  # change case of upper
x.lower() # change to lower case
x.split() # split hello world on white space.
x.split('i') # split on i
print ('this is a string {}' .format('INSERTED')) # add INSERTED
print ('The {2} {1} {0}' .format ('fox', 'brown', 'quick'))
print ('The {q} {b} {f}' .format (f='fox', b='brown', q='quick'))
result=100/777
print ("The result was {r}" .format(r=result))
# formating a floating point


# Float formating follows "{value:width.precision f}"
print ("The result was {r:1.4f}".format(r=result))
name ="simon"
age=3
print (f'Hello, hist name is {name}')
print (f'{name} is {age} years old')
print (f'Python {"rules!"}')
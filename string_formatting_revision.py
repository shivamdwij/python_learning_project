mystring="Hello world"
print(mystring)


# indexing 

mystring="My name is Shivam"
print(mystring[3])

#let try to print 'm' from Shivam

print(mystring[-1])   # reverse  can be done like this

# or 
print(len(mystring))
print(mystring[16])

mystring="abcdefghigk"

print(mystring[2:])    # slicing, prints all results after index 2 

# sytax print(mystring[START:STOP])  remember STOP does not include the index mentioned in the STOP

print(mystring[2:5])

# IMP - Step size
#syntax print(mystring[START:STOP:STEP SIZE]) This means it will go from start to stop but jumps the numbers mentioned in the step size

print(mystring[0:9:2])

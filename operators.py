# Operators

# range operator  - range is actually a generator that genrates values.git 

for num in range(1,11):
    print(num)

for num in range(1,11,2):    # ,2 will add a hop to print every number with a gap of two numbers
    print(num)

# enumerate function  - this function will proivde the values along with the index number
word='abcde'
for index,letter in enumerate(word):     # unpacking can also be used here
    print(index)

# zip funtion:- this function will map multiple list with each other
#remarks:- the list mapping will only be done with same list size extra items will not be mapped and be ignored

list1=[1,2,3,4,5]
list2=['a','b','c','d']

for lit in zip(list1,list2):
    print(lit)

print(min(list1))
print(max(list1))   #min/max built-in function can be used
print(f'this is a maximum number present in the list {max(list1)}') # string formatting
from random import shuffle
shuffle(list1)
print(list1)

# input fuction

name=input('What is your name?')  # input by default accept the input into the string, for all other format we need to hanlde them
print(name)


# list comprehension

list_com=[num for num in range(1,11)]
print(f'here is the list comprehension example {list_com}')

# playing around more with list comprehension, if I want the square of every number in thelist

list_com=[num**2 for num in range(1,11)]
print(f'here is the list comprehension example {list_com}')

# addion if statement in the list comprehension
list_com=[num**2 for num in range(1,11) if num%2==0]
print(f'here is the list comprehension with if statement {list_com}')

# empty list

far=[]
celcius=[0,10,20,30,40,50]
for temp in celcius:
    far.append(((9/5)*temp) + 32)
print(far)

# the above code can be written in one line using list comprehension

far=[(((9/5)*temp) + 32) for temp in celcius]
print(f'this is using list comprehension {far}')



# for this we have two methods
# 1. . format() methods
# 2. f-string (formattted strings literals)
# Let's start with .format method

my_string="This is a string"

# way 1:-
#syntax:- "string1{}.format(string2)"
mystring='This is a string {}'.format('inserted')
print(mystring)

# way 2:-
#syntax:- "string1{index postion} {index postion} {index postion}".format('string1','string2','string3')  --> string1 is at index position 0 string 2 is at index position 1 and so on

mystring='My {} {} {}'.format('name', 'is','Shivam')
print('result--> ' + mystring)

# way 3:- we can assign a the string as an value to a variable, this will help increase the readability of the code
#syntax:-  "my {a} {b} {c}".format(a='string1',b='string1',c='string1')

mystring='My {a} {b} {c}'.format(a='name',b='is',c='Shivam')
print("Final Result --> " + mystring)

#sepcial concept:-
# Float formatting flows
#syntax:- "The output is {value:width.precision f}".format(f='result'), --> width is the space between string and output

result=100/777
mystring="The output is {r:10.4f}".format(r=result)   # here is 10 represents the gap between both the strings and 4f represents the allowed values after decimal
print("this is it" + mystring)

#way 4 :- formatted string literals refer to #2 on the top of page

name='Shivam Trivedi'
mystring=(f'My name is {name}')  # this is in new python 3.6 and higher versions
print(mystring)


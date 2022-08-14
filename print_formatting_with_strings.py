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


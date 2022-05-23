# 1



def myfunc():
    print("Hello World")

#2

def myfunc(name):
    #return 'Hello {}'.format(name)
    print('Hello {}'.format(name))

#3

def myfunc(a):
    if a == True:
        return "Hello"
    elif a == False:
        return "Goodbye"

#4

def myfunc(x,y,z):
    if z==True:
        return x
    elif z==False:
        return y

#5

def myfunc(x,y):
    return x+y

#6

def is_even(x):
    if x%2==0:
        return True
    else:
        return False

#7

def is_greater(x,y):
    if x>y:
        return True
    elif y<=x:
        return False

#8

def myfunc(*args):
    return sum(args)

#9

def myfunc(*args):
    a=[]
    for num in args:
        if num%2==0:
            a.append(num)
        else:
            pass
    return a

#10

def myfunc(mylist):
    final_list=[]
    for i in range(len(mylist)):
        if i%2==0:
            final_list.append(mylist[i].upper())
        else:
            final_list.append(mylist[i].lower())
    return ''.join(final_list)   # .join() is a string method 
mylist=('a','b','c','d','e')

print(myfunc(mylist))   

# 50 FUNCTION PRACTICE EXERCISE ----------

#1. LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd


def lesser_of_two(a,b):
    if a%2==0 and b%2==0:
        if a-b>0:
            return b
        elif b-a>0:
            return a
    elif a%2!=0 or b%2!=0:
        if a-b>0:
            return a
        elif b-a>0:
            return b

results = lesser_of_two(4,15)
print(results)

# efficient way to write this function is:-
"""
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)            USING MIN AND MAX FUNCTION
    else:
        return max(a,b) """


#2 ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def same_letter(text): 
    two_words=text.lower().split()
    first=two_words[0]
    second=two_words[1]
    return two_words[0]==two_words[1]

    # EFFICIENT WAY
    '''def animal_crackers(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]'''

#3 MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a,b):
    if a+b==20:
        return True
    elif a==20 or b==20:
        return True
    else:
        return False

results = makes_twenty(10,10)
print(results)

 # SLEEKER WAY TO ACHIEVE ABOE
''' def makes_twenty(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
'''

# LEVEL 1 PROBLEMS
#1.1 OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def mcd(text):
    first_letter=text[0]
    inbetween_words=text[1:3]   # indexing & slicing
    fourth_letter=text[3]
    rest=text[4:]
    return first_letter.upper() + inbetween_words + fourth_letter.upper() + rest

text='macdonalds'

results = mcd(text)
print(results)

# SLEEKER WAY 
""" def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'  """

# 1.2 MASTER YODA: Given a sentence, return a sentence with the words reversed

def reveb(st):
    splitting = st.split()
    rev = splitting[::-1]     # list slicing and indexing here -1 is to set the reverse order
    st =' '.join(rev)   # .join() is used to join multiple values in a list 
    return st

results=reveb('I am a good boy')

print(results)

# BONUS QUESTIOIN:- ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))  #abs is the function that provides the absolute values of a number








            

        





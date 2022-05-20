example=[1,2,3,4,5,6]
from random import shuffle # shuffle the items within a list

def shuffle_list(a):
    shuffle(a)
    return a

results=shuffle_list(example)
print(results)


#-------------------------GAME TO CHECK CAPITAL O IS AT WHICH POSITION-------------------------------
my_list=['','','O']

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number: 0,1 or 2")
    return int(guess)
    
def check_guess(my_list,guess):
    if my_list[guess] == 'O':    # check guess in any of the index postion of the my_list
        print("CORRECT!!")
    else:
        print("WRONG GUESS!")
        print(my_list)


# CREATE A LIST

my_list=['','O','']

# SHUFFLE LIST
mixedup_list=shuffle_list(my_list)

# PLAYER GUESS
user_guess=player_guess()

# CHECK GUESS

check_guess(mixedup_list,user_guess)








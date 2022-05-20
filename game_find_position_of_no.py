from random import shuffle

my_list=['','','O']

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number: 0,1 or 2----->")
    return int(guess)
    
def check_guess(my_list,guess):
    if my_list[guess] == 'O':    # check guess in any of the index postion of the my_list
        print("CORRECT!!")
        print(my_list)
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


# ------- CORRECT FLOW OF WRITING CODE------------------
# 1. DEF FUNTION AT THE TOP
# 2. WRITE LOGIC TO CALL THE FUNCTIONS SEQUENCIALLY AFTER #1
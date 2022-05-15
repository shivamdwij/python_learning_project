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


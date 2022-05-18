from sqlalchemy import values


my_list=[1,2,3,4,5,6,7,8,9]

for num in my_list:  # for loop
    print(num)
print("--------------------------")
for num in my_list:    # control flow 
    if num % 2 ==0:
        print(f'Even Number:{num}')    # string formatting
    else:
        print(f'Odd Number: {num}')


tup = [(1,2),(2,3),(3,4),(4,5)]

for a,b in tup:      #unpacking technique is used here
    print(b)

dict={'k1':1,'k2':2,'k3':3}
for item in dict:
    print(item)

dict={'k1':1,'k2':2,'k3':3}
for item in dict.items():
    print(item)

dict={'k1':1,'k2':2,'k3':3}
for key,values in dict.items():          #unpacking technique is used here
    print(values)


#while loop

a=0 
while a < 10:
    if a==5:
        break    # break, continue & pass can be used along with while loop
    print(a)
    a += 1

# Operators

# range operator  - range is actually a generator that genrates values.git 

for num in range(1,11):
    print(num)

for num in range(1,11,2):    # ,2 will add a hop to print every number with a gap of two numbers
    print(num)
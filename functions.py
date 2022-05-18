from pickle import TRUE


def mysum(a,b):
    print(a+b)
mysum(10,20)

def mysumreturn(a,b):
    return a+b

return_result=mysumreturn(10,20)
print(return_result)

#Differne between print and return in function is print will allow you to only print the value, 
#Return will allow you to save the output into a variable which can be used further into your code

#-----------------Functions with Logic----------------------------------

# create a function to check even number in a list

def check_even(num):
    for temp in num:
        if temp % 2 == 0:
            return True
        else:
            pass

result=check_even([1,2,3,4,5,5,6,7,8,9,10])
print(result)

# create a function to return all even numbers in a list

def create_list_even_no(num):
    even_list = []
    for temp in num:
        if temp%2==0:
            even_list.append(temp)   # This will append the even number to the even_list 
        else:
            pass    # This pass is ensuring we are not coming out of the loop unless we are getting an even number or the end of the list
    return even_list

result1=create_list_even_no([1,3,5,8,10,12])
print(result1)






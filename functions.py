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
    even_list = []             # this is an empty list, also know as placeholder list
    for temp in num:
        if temp%2==0:
            even_list.append(temp)   # This will append the even number to the even_list 
        else:
            pass    # This pass is ensuring we are not coming out of the loop unless we are getting an even number or the end of the list
    return even_list

result1=create_list_even_no([1,3,5,8,10,12,14])
print(result1)


#----------------------Tupples unpacking with function-----------------------

# we need to find out which is giving maximum number of hours to our company

work_hours=[('shivam',1000),('suvidha',200),('mrity',400)]

def employee_check(work_hours):
    current_max=0
    employee_name=''
    for employee,hours in work_hours:
        if hours>current_max:
            current_max=hours
            employee_name=employee
        else:
            pass
    return (employee_name,current_max)

final_list=employee_check(work_hours)
name,hours=employee_check(work_hours)    # unpacking the results 
print(final_list)
print(name)                              # unpacked results
print(hours)                             # unpacked results






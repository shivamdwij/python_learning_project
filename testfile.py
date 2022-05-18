def check_even(num):
    for temp in num:
        if temp % 2 == 0:
            return True
        else:
            pass
            
result=check_even([1,2,3,4,5,5,6,7,8,9,10])
print(result)
my_string = "Hello World"
b=str(my_string[0:6])
b = b + " Shivam" # string concatenation
print(b.lower()) # upper method
print(b.upper()) # lower method

print("Shivam {} {} {} {}".format('is','a','good','boy')) # .format method for string concatenation
print("Shivam {f} {a} {g} {b}".format(f='is',a='a',g='good',b='boy')) # .format method by assigning value to each string making it more readble
#print("Suvidha {} {} {} {}".format ())
result=107.29287627
print("This is the result {r:2.3f}".format(r=result))   # r is variable assinged, 2 is space from the string, 3 is for permissble decimal values, f for string formatting

name="shivam"
age=29
color="brown"
print(f"{name} is {age} yeard old and has {color} complexion") #new way of formatting string

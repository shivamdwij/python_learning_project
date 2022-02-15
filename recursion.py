from tkinter.tix import INTEGER


def factorial(x):
    if (x==1):
        return 1
    else:
        return x*(factorial(x-1))  # using the function itself in the function

result=factorial(6)
print(result)   # print factorial of 6, few more............//


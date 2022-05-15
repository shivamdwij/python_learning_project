# tuples

t=(1,2,3)
print(t)

# sets -> Sets are unorderred collections of unique items
myset= set()
print(myset)

myset.add(1)
print(myset)

myset.add(2)
print(myset)

myset.add(2)  # if we add 2 again, the set will only show 2 once since it only possess unique items
print(myset)

type(True)
print(type)

myfile=open("C:\\shivam_trivedi\\python\\python_scripts\\python_learning\\text.txt")   # it requires double backward slash in the folder path
content=myfile.read()
print(content)
myfile.close()
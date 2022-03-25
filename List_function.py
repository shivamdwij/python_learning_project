# list function

shivam=["Job","Is","At","magicpin"]
Trivedi=["Where", "is","he"]

print(shivam)
print(Trivedi)
print(shivam+Trivedi)
shivam.append("NPF") # add any item at the end of the list
print(shivam)
shivam.append("new_append")
print(shivam)

# .pop function deletes the last item from the list, below are few examples
shivam.pop()
print(shivam) # item 'new_append' is not deleted from the list, you can also provide the index of the item you want to delete

shivam.pop(2)
print(shivam)  #At is deleted here

# .sort function will sort the list, for example

alpha_b=["b","a","d","c"]
alpha_b.sort()
print(alpha_b)  # sort the list in the alphabetical order

# strings are immutable, this mean you cannot assign any value to any index of the string

# for example
# let say you have a string a = "hello" and you want to replace h with a, you cannot do this, this is called immutability
# You can do the above by string concatenation, below is the example

my_name="Shivam"

# you have to replace "m" with "t"

last_one_letters=my_name[:-2]
print(last_one_letters)

# now we can do string concatenation by using (+) symbol

print(last_one_letters + " t")

# reading and writing to a file

with open('C:\\shivam_trivedi\\github\\python_learning_project\\text.txt',mode='r') as r:
    print(r.read())


with open('C:\\shivam_trivedi\\github\\python_learning_project\\text.txt',mode='w') as w:
    text = w.write("This is the override text")
    print(text)

with open('C:\\shivam_trivedi\\github\\python_learning_project\\text.txt',mode='r') as r:
    print(r.read())

# student example

class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def get_data(self):
        self.name=input("Enter name")
        self.age=input("Enter age")

    def print_data(self):
        print(self.name)
        print(self.age)

student1=Student("","")
student1.get_data()
student1.print_data()


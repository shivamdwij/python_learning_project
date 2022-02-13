class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_data(self):
        self.name=input("Enter the name")
        self.age=input("Enter the age")

    def print_data(self):
        print(self.name)
        print(self.age)

student1=Student("","")
student1.get_data()
student1.print_data()

class Science_student(Student):    # Inherited class
    def science(self):
        print("This is inheritance")

a=Science_student("","")        # object of inherited class
a.get_data()
a.print_data()




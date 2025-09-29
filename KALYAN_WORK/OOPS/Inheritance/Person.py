class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks


    def displayInfo(self):
        print("Name: ",self.name," Age: ",self.age,"marks: ",self.marks)


s1 = Student("kalyan",21,75)
s1.displayInfo()

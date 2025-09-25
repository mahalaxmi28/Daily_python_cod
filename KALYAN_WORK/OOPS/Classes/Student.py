class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def showMArks(self):
        print(self.marks)

    def avgMarks(self):
        sum = 0;
        for i in self.marks:
            sum = sum+i

        avg = sum/len(self.marks)
        print("Average marks of ",self.name ," are ",avg)




student1 = Student("kalyan",20,[78,64,70,82])

student1.avgMarks()

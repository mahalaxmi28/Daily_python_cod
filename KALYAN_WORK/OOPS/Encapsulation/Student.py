class Student:
    def __init__(self,name,__marks):
        self.__marks = __marks
        self.name = name

    def setMarks(self,marks):
        if marks>0 and marks<100:
            self.__marks = marks
        else:
            print("Invalid marks") 

    def getMarks(self):
        print(self.__marks)


s1 = Student("kalyan",78)
s1.getMarks()
s1.setMarks(85)       
s1.getMarks()
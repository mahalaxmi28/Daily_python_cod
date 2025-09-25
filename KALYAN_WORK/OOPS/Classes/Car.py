class Car:
    def __init__(self,brand,color,year):
        self.brand = brand
        self.color = color
        self.year = year

    def showDetails(self):
        print(f"Car brand: {self.brand} , Car Color: {self.color}, Car manfacture year: {self.year}")

car1 = Car("BMW","blue",2010)
car2 = Car("Mercedes","black",2016)


car1.showDetails()
car2.showDetails()
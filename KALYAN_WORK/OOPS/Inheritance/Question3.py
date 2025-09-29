class Vehicle:
    def __init__(self,model,brand):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, model, brand):
        super().__init__(model, brand)

    def displayInfo(self):
        print("Car brand: ",self.brand,"Car model: ",self.model)


class Bike(Vehicle):
    def __init__(self, model, brand):
        super().__init__(model, brand)

    def displayInfo(self):
        print("Bike brand: ",self.brand,"Bike model: ",self.model)

car1 = Car("i20","maruti")
bike1 = Bike("Himalayan","Royal Enfield")
car1.displayInfo()
bike1.displayInfo()
        
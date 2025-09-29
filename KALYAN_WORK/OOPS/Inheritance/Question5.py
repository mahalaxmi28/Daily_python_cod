class Animal:
    def eats():
        print("Animals eat food")

class Mamals(Animal):
    def walks(self):
        Animal.eats(self)
        print("Mamals can walk and swim")

class Dog(Mamals):
    def barks(self):
        Mamals.walks(self)
        print("DOg barks")

d1 = Dog()

d1.barks()
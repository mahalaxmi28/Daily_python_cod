class Father:
    def __init__(self):
        pass
    def skills():
        print("Driving skills")

class Mother:
    def skills():
        print("Cooking skills")

class Child(Mother,Father):
    def skills(self):
        Father.skills()
        Mother.skills()

        print("Studying skills")

c1 = Child()
c1.skills()
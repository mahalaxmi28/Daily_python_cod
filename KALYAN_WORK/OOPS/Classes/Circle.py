class Circle:
    radius = 10
    def __init__(self):
        pass

    def perimeter(self):
        print(2*3.14*self.radius)

c1 = Circle()
c1.radius = 15
c1.perimeter()
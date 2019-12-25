import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def __add__(self, another_circle):
        return Circle( self.radius + another_circle.radius )
c1 = Circle(4)
print(c1.getRadius())
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + c2 
print(c3.getRadius())
print(c2.area())
c4 = Circle(6)
print(c4.area())

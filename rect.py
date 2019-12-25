class Rectangle():
    def __init__(self, l, b):
        self.length = l
        self.breadth  = b

    def rectangle_area(self):
        return self.length*self.breadth

newrect = Rectangle(10, 10)
print("area of rectangle = ",newrect.rectangle_area())

import math
class circle():
	def __init__(self,radius):
		self.radius=radius
    def area (self):
        area = math.pi*(self.radius**2)
        return area
    def perimeter(self):
                   perimeter=4*math.pi*self.radius
                   return perimeter
	def display1(self):
	    print ("radius",self.radius)
r=circle(float(input(' Please Enter the radius of a circle: ')))
r.display1()
print ("area of circle=",area)
print ("perimeter of circle",perimeter)

)






























































































































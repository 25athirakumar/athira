class Employee:
   'Common base class for all employees'
   
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      
   
   
   def displayEmployee(self):
      sum=self.name +self.salary
      print sum
      
   def displayEmployee1(self):
      sum=self.name -self.salary
      print sum

"This would create first object of Employee class"
emp1 = Employee(3, 2000)
"This would create second object of Employee class"
emp2 = Employee(5, 5000)
emp1.displayEmployee()
emp1.displayEmployee1()
emp2.displayEmployee()

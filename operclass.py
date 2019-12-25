class operations:
   
   
   def __init__(self, a, b):
      self.a = a
      self.b = b
      
   
   
   def op(self):
      sum=self.a +self.b
      print (sum)
      
   def op1(self):
      sub=self.a -self.b
      print (sub)
      
   def op2(self):
      mul=self.a *self.b
      print (mul)
    
   def op3(self):
      div=self.a /self.b
      print (div)


emp1 = operations(3, 2)
emp2 = operations(5, 50)
emp1.op()
emp1.op1()
emp2.op2()
emp2.op3()

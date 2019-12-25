class operations:
	
	def __init__(self,a,b):
		self.a = a
		self.b = b
	def add(self):
      sum= self.a +self.b
      print sum
    def sub(self):
      sub= self.a -self.b
      print sub
    def multi(self):
      mul= self.a *self.b
      print mul
    def divi(self):
      div= self.a /self.b
      print div
a1=operations(2,4)
a2=operations(55,33)
a1.add()
a1.sub()
a2.multi()
a2.divi()
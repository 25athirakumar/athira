class student():
	def __init__(self,name,regno):
		self.name=name
		self.regno=regno
	def display1(self):
		print (self.name)
		print (self.regno)
class college(student):
	def __init__(self,name,regno,branch,batch):
		self.branch=branch
		self.batch=batch
		student.__init__(self,name,regno)
	def display2(self):
		print(self.branch)
		print(self.batch)
stu1=college('athi',23,'ece',22)
stu1.display1()
stu1.display2()

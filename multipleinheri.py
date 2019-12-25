class student():
	def __init__(self,name,regno):
		self.name=name
		self.regno=regno
	def display1(self):
		print ("name",self.name)
		print ("regno.",self.regno)
class college(student):
	def __init__(self,name,regno,branch,batch):
		self.branch=branch
		self.batch=batch
		student.__init__(self,name,regno)
	def display2(self):
		print("branch",self.branch)
		print("batch",self.batch)
class university(student):
	def __init__(self,name,regno,branch,batch):
		self.branch=branch
		self.batch=batch
		student.__init__(self,name,regno)
	def display3(self):
		print("branch",self.branch)
		print("batch",self.batch)
stu1=college('athi',23,'ece',22)
stu1.display2()
stu1.display1()
stu1=university('sri',51,'ece',20)
stu1.display3()
stu1.display1()



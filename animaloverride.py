class Animal:
	def breathe(self):
	   print("I breathe oxygen.")
	def feed(self):
	   print("I eat food.")
	    
class Herbivorous(Animal):
    def breathe(self):
	   print("I breathe oxygen like all animals.")
	def feed(self):
	   print("I eat only plants. I am vegetarian.")
herbi = Herbivorous()
herbi.feed()
herbi.breathe()
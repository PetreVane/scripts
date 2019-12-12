
class Parent():
	def __init__ (self, last_name, eye_color, age):
		print "Parent constructor has been called"
		self.last_name = last_name
		self.eye_color = eye_color
		self.age = age

	def show_info(self):
		print "Last name: " + self.last_name
		print "Eye color: " + self.eye_color
		print "Age: " + self.age

#ioana = Parent("Radu", "brown", "29")
#ioana.show_info()

class Child(Parent):
	def __init__ (self, last_name, eye_color, age, number_of_toys):
		print "Child constructor has been called"
		Parent.__init__(self, last_name, eye_color, age)
		self.number_of_toys = number_of_toys

	def show_info(self):
		print "Last name: " + self.last_name
		print "Eye color: " + self.eye_color
		print "Number of toys: " + self.number_of_toys


petre_vane = Child("Vane", "brown", "five","10")
petre_vane.show_info()

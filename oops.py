# Python Object-Oriented-Programming

# To create a class we use a keyword called <classs>
# self is mandatory parameter when working with classes

#class:
	# class is a blueprint for creating instances
	# classes allows us to organize and manage our code in a 
	# easier and more sophisticated way.

# common terms used when working with classes are,
'''
instances, methods, functions, magic_methods or dunder methods,
attributes, object is not callable
'''

#__init__ is a special method in python will will be
# called when a class is invoked.

# Anything inside the __init__ function will be executed first

'''
The self keyword:

'''



#simple class:
class Employee:
	pass
	
	#() these not mandatory when working with classes.

#A simple instance example

emp1 = Employee()
emp2 = Employee()


#emp1 and emp2 are the instances for our Employee class
#You can create any number of instance you would like.

#Instance variables manually:
emp1.name = "Sush"
emp1.age = 27
emp1.mail = 'sush27.email.com'
emp1.pay = 50000

emp2.name = "Shiva"
emp2.age = 24
emp2.mail = 'Shiva24.email.com'
emp2.pay = 50000

# print(emp1.name)
# print(emp2.name)

class Exe:
	def __init__(self):
		pass
e = Exe() 

class Developer:

	def __init__(self, first, last, role):
		self.first = first
		self.last = last
		self.role = role
		self.pay = 60000

	def fullname(self):
		print("Full name is {}, {}".format(self.first, self.last))

	def print_pay(self):
		print('Pay {}'.format(self.pay))

d1 = Developer("Shiva", 'M', 'PythonDeveloper')
d2 = Developer("Sush", 'R', 'DevopsEngineer')
print(d1.first)
print(d2.first)
d1.fullname()
d1.print_pay()

d1.first = 'Mith'
print(d1.first)

d2.pay = 900000
print(d2.pay)

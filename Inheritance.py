class Employee:
	def __init__(self, first, last, email):
		self.first = first
		self.last = last
		self.email = email

class Developer(Employee):
	def __init__(self, first, last, email, prog_lang):
		super().__init__(first, last, email)
		self.prog_lang = prog_lang

class Manager(Employee):
	def __init__(self, first, last, email, employees):
		super().__init__(first, last, email)
		self.employees = employees

	def add_emp(self, emp):
		pass
	def delete_emp(self, emp):
		pass
	def get_employees(self):
		pass

d1 = Developer("Shiva", 'M', 'siva@email.com', 'Python')
# print(d1.prog_lang)
# print(help(d1))

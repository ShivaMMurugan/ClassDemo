class Students:
	#self > convention, self > initialize
	def __init__(self, first, last, email): #instance variables
		# dunder method, special method
		self.first = first
		self.last = last
		self.email = email

st = Students("Shiva", "M", "siva.m@email.com")
print(st.first)
print(st.last)
print(st.email)
m = Students("SivaK", "R", "sivaK.m@email.com")

def HttpCodes:
	def success(self):
		return 200
	def not_found(self):
		return 404
	def internal_server_error(self):
		return 501
	def unauthorized(self):
		return 409

def do_request:
	url = ()
	if url.status_code != HttpCodes.success:
		print("Not a valid address")

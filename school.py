
class student:
	def __init__(self,name,gpa1,gpa2):
		self.name = name
		self.gpa1 = gpa1
		self.gpa2 = gpa2
		self.cgpa = round((gpa1 + gpa2)/2,2)
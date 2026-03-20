class Student:
	def __init__(self,n,a,m):
		self.n=n 
		self.a=a 
		self.m=m 
	def __str__(self):
		return f"name: {self.n} age: {self.a} mark: {self.m}"
s1=Student('PHIL',34,77)
s2=Student('JOEY',34,77)
s3=Student('JAY',34,77)
print(s1)
print(s2)
print(s3)
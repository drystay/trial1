#instance variable 
class Demo:
	c=100
	def __init__(self,):
		self.a=10
		print(self.a)
	def show(self):
		self.b=30
		print(self.b)
d=Demo()
print(d.__dict__)
d.show()
print(d.__dict__)
print(d.a,d.b,d.c,Demo.c)
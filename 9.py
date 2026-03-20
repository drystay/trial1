class Demo:
	a=10
	def __init__(self):
		self.b=20
ob1=Demo()
ob2=Demo()
print(ob1.a,ob1.b)
print(ob2.a,ob2.b)
ob1.b=30
ob2.b=40
Demo.a=50
print(ob1.a,ob1.b)
print(ob2.a,ob2.b)
class Demo:
	@classmethod
	def add_var(self):
		Demo.var=100
		print(Demo.var)

	def delete_class_var(self):
		del Demo.var
		print("deleted")
d=Demo()
d.add_var()
d.delete_class_var()

class Demo:
	pass
d=Demo()
d.a=10
print(d.a)
del d.a

#in a constrcutor 
class Demo:
	def __init__(self,value):
		self.x= value 
	def __del__(self):
		def self.x #destructor 
d=Demo(10) 
print(d.x)
del d.x
print(d.x) #here it wont print as deleted

class Demo:
	def set(self,value):
		self.x=value
	def delete(self):
		del self.x
d=Demo()
d.set(100)
print(d.x)
d.delete()

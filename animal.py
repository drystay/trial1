class Animal:
	def show(self):
		print("makes sound")	
class Cat(Animal):
	def show(self):
		super().show()
		print("meow")
class Dog(Animal):
	def show(self):
		super().show()
		print("bark")
c=Cat()
c.show()
d=Dog()
d.show()
a=Animal()
a.show()

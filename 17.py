from abc import ABC, abstractmethod
class Animal(ABC):
	def sound(self):
		pass
class Dog(Animal):
	def __init__(self):
		print("this is a dog class")
	def sound(self):
		print("dog barks")
class Cat(Animal):
	def __init__(self):
		print("this is a cat class")
	def sound(self):
		print("cat meows")
class Horse(Animal):
	def __init__(self):
		print("this is a horse class")
	def sound(self):
		print("horse neighs")
d=Dog()
d.sound()
c=Cat()
c.sound()
h=Horse()
h.sound()
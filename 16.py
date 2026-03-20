class Mystr(str):
	def __new__(cls,value):
		print("inside")
		obj = super().__new__(cls,value.upper()) #upper case 
		return obj
	def __init__(self, value):
		print("inside __init__")
s= Mystr("my name is dristi")
print(s)
print(type(s))

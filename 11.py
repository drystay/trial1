class Test:
	def __init__(self):
		self.a=10
		self.__b=20 #private
	def show(self):
		print("show function")
		self.__disp()
	def __disp(self):
		print("private display function")
t=Test()
print(t.a)
t.show()
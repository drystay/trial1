class Test:
	def __init__(self,x,y):
		print("constructor")
	def show(self):
		print(self.x)
		print(self.y)
	def __del__(self):
		print("destructor")
t=Test(44,55)
t.show()
t1=Test()
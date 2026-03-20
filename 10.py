class Demo:
	c=0
	def __init__(self):
		Demo.c=1
		self.a=1
	def up(self):
		Demo.c=Demo.c+1
		self.a=self.a+1
	def show(self):
		print(self.a,Demo.c)
d=Demo()
d1=Demo()
d2=Demo()
d.up()
d1.up()
d2.up()
d.show()
d1.show()
d2.show()
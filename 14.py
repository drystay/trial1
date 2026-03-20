import sys
class Mycqueue:
	def __init__(self,max):
		self.L=[0]
		self.front=-1
		self.rear=-1
		self.max=max

	def enqueue(self,ele):
		if (self.rear +1) % self.max == self.front:
			print("CQ overflow")
			return
		if self.front==-1:
			self.front=0
			self.rear=0
		else:
			self.rear = (self.rear+1)% self.max
		self.L[self.rear]=ele 
		print(ele," inserted ")
	def dequeue(self):
		if self.front==-1:
			print("CQ underflow")
			return
		print("removed ele ",self.L[self.front])
		if self.front == self.max-1:
			self.front=0
			return
		if self.front == self.rear:
			self.front=-1
			self.rear=-1
		else:
			self.front = (self.front+1)% self.max

	def peek(self):
		if self.front == -1:
			print("CQ underflow")
			return
		print("top ele ",self.L[self.front])

	def disp(self):
		if self.front == -1:
			print("CQ underflow")
			return
		if self.front <=self.rear:
			for i in range(self.front,self.rear+1,-1):
				print(self.L[i])
		else:
			for i in range(self.front,self.max,-1):
				print(self.L[i])
			for i in range(0,self.rear,-1):
				print(self.L[i])

m=Mycqueue(6)
while True:
	print("enter your choice from \n 1.enqueue \n 2. dequeue \n 3.Seek \n 4.display \n 5.exit")
	ch= int(input())
	if ch==1:
		m.enqueue(int(input()))
	elif ch==2:
		m.dequeue()
	elif ch==3:
		m.peek()
	elif ch==5:
		sys.exit()
	elif ch==4:
		m.disp()
	else:
		print("invalid")

	
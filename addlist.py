l=[10,20,30,40]
pos=int(input("enter the position that you want to enter \n"))
if pos>len(l):
	print("invalid position")
else:
	for i in range(0,pos):
		i=i+1
	l[i]=int(input("enter element of your choice \n"))
print(l)

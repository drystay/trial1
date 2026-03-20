#search an element and delete all location 
l=[]
s=eval(input("enter the size \n"))
for i in range(0,s):
	print("enter element ", i+1)
	l.append(eval(input()))
check=eval(input("enter what element you want to remove \n"))
i=0
c=0
while i < len(l)-c:
	if l[i]==check:
		c=c+1
		for j in range(i,len(l)-1-c):
			l[j]=l[j+1]
	else:
		i+=1
for i in range(len(l)-1,len(l)-c-1,-1):
	del(l[i])
for i in range(0,len(l)):
	print(l[i],end='')
print(l)
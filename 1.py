#search an element and remove w/o predefined without new list 
l=[]
s=eval(input("enter the size \n"))
for i in range(0,s):
	print("enter element ", i+1)
	l.append(eval(input()))
check=eval(input("enter what element you want to remove \n"))
i=0
while i < len(l):
	if l[i]==check:
		for j in range(i,len(l)-1):
			l[j]=l[j+1]
		break
	else:
		i+=1
del l[j+1]
print(l)
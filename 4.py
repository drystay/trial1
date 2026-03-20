#max no of times occur
L=[]
max=0
ele=0
size=eval(input("enter the size of the list \n"))
for i in range(0,size):
	print("enter element ",i+1)
	L.append(eval(input()))
i,j=0,0
for i in range(0,len(L)):
	c=1
	if L[i]==-1:
		continue
	for j in range(i+1,len(L)):
		if L[j]==-1:
			continue
		if L[i]==L[j]:
			c=c+1
			L[j]=-1
		if c>max:
			max=c
			ele=L[i]
print(ele," occur ",max," times")
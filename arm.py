num=int(input("Enter a number"))
p=0
temp=num
arm=0
while temp!=0:
	p=p+1
	temp=temp//10
temp=num
while temp!=0:
	r=temp%10
	arm=arm+(r**p)
	temp=temp//10
if arm==num:
	print(num," is a armstrong number")
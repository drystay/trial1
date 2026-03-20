l=[10,20,30,40,0]
pos=0
check=int(input("enter element you want to search \n"))
for i in range(0,len(l)-1):
  if l[i]==check:
    pos=i
    if pos+1>len(l):
      print("invalid position")
  for i in range(len(l)-1,pos-1,-1):
    l[i]=l[i-1]
  l[pos-1] = int(input("enter element you want \n"))
print(l)
l1=[[1,2],[3,4]]
l2=[[2,2],[3,3]]
l3=[ [ l1[i][j] + l2[i][j] for j in range(len(l1[i]))] for i in range(len(l1))]
print(l3)
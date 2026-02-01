p = [[""]*5 for i in range(10)]#10x5
#print(p)
for i in range(10):
    for j in range(5):
        p[i][j] = "({0},{1})".format(i,j)

for i in range(10):
    for j in range(5):
        print(p[i][j],end=" ")
    print()    

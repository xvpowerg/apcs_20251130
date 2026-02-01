x = [5,15,25,35,45]
for data in x:
    print(data,end=" ")
print()
for i in range(len(x)):
    print(i,x[i],end=",")
print()

x.append(100)
print(x)
x[2] = 20
print(x)
x.remove(20)
print(x)

m = x.pop()
print("pop:",m)
print(x)
m = x.pop(2)
print("pop(2):",m)
print(x)















#內容為1~10的List如何實現
y = []
for i in range(1,11):
    y.append(i)
print(y)    
#內容為1~10的偶數List如何實現
z = []
for i in range(1,10):
    if i % 2 == 0:
        z.append(i)
print(z)

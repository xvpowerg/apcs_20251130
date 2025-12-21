myList = [lambda x:x+2,lambda x: x **2 ,lambda x : x - 2]

a = 9
for func in myList:
    print(func(a))

def myFilter(func,myList):
    result = []
    for v in myList:
        if func(v):
            result.append(v)
    return result

myList = [2,4,5,7,9,11,25,63,18]

ans1 =  myFilter(lambda x : x % 2 == 0,myList)
print(ans1)
ans2 = myFilter(lambda x:x > 10,myList)
print(ans2)

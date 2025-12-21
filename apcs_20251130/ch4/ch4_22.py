def func(myList,n):
    result = []
    for i in myList:
        if i > n:
            result.append(i)
    return result

myList = [7,8,11,2,5,3]
ans = func(myList,4)
print(ans)

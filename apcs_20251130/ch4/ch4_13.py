def func(theList):
    result = []
    print("theList:",theList)
    for v in theList:
        result.append(v + 2)    
    return result

theList = [1,2,3,4]
# 3 4 5 6
ans = func(theList)
print(ans)


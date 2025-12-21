def func(thenList,myFunc):
    result = []
    for v in thenList:
        result.append(myFunc(v))
    return result

def func1(v):
    return v ** 2
def func2(v):
    return v - 5

myList = [1,2,3,4,5]

r1 = func(myList,func1)
r2 = func(myList,func2)

print(r1)
print(r2)

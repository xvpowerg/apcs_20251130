import random

def mySample(data,count):
    myLen = len(data)
    result = []
    indexSet = set()
    while len(indexSet) != count:
        index = random.randint(1,myLen) - 1
        indexSet.add(index)
    
    for i in indexSet:    
        result.append(data[i])
    return result
fruits = ['香蕉', '蘋果', '橘子', '西瓜']
myList = mySample(fruits,2)
print(myList)

import random

def mySample(data,count):
    
    result = []
    for i in range(count):
        myLen = len(data)
        index = random.randint(1,myLen) - 1
        result.append(data.pop(index))
    return result
fruits = ['香蕉', '蘋果', '橘子', '西瓜']
myList = mySample(fruits,2)
print(myList)

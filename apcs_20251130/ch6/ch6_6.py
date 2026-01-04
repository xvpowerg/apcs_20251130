import random

def mySample(data,count):
    myLen = len(data)
    result = []
    for i in range(count):    
        index = random.randint(1,myLen) - 1
        result.append(data[index])
    return result
fruits = ['香蕉', '蘋果', '橘子', '西瓜']
myList = mySample(fruits,2)
print(myList)

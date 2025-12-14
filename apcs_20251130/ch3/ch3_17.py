listOfTuple = [(5,6),(7,10),(8,13),(7,2)]
myMax = -1
mySum = 0
for v1,v2 in listOfTuple:
    if v1 > myMax:
        myMax = v1
    if v2 > myMax:
        myMax = v2
    mySum += v1 + v2
print("max:",myMax)
print("sum:",mySum)
##找出數字最大
#數字的總和

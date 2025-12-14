## 請寫一個程式，顯示由1至1000之間的費伯那西數列
# 1  2  3  4  5  6  7    8   9  19    
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
myMax = 60
num1,num2 = 1,1
print(num1,num2,sep=", ",end = "")
nextNum = num1 + num2

while  nextNum < myMax:
    print(f", {nextNum}",end="")
    num1 = num2
    num2 = nextNum
    nextNum = num1 + num2
    

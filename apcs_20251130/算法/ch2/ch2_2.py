a1 = int(input("首項"))
d = int(input("公差"))
n = int(input("項數"))
sum1 = 0
for i in range(n):
    ai = a1 + i * d
    sum1 += ai
print("sum:",sum1)    

print("遞迴")
def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) + d
sum2 = 0
def getSn(n):
    if n == 1:
        return a1
    else:
        an = getAn(n)
        return getSn(n-1) + an
print("sum:",getSn(n))

n = int(input("輸入n"))
sum1 = 0
for k in range(2,n+1):
    ai = (k - 1) * k
    sum1 += ai
print(sum1)    

def getSum(n):
    if n == 1 or n == 0:
        return 0
    else:
        return getSum(n-1) + n * (n-1)
print(getSum(n))    

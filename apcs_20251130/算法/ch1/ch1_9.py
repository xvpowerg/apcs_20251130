a1 = int(input("首項"))
r = int(input("公比"))
n = int(input("項數"))
print("for loop")
for i in range(n):
    print(a1 * r ** i,end=" ")
def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n - 1) *ｒ
print()
for i in range(1,n+1):
    print(getAn(i),end=" ")

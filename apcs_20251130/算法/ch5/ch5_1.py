def myLog(a,b,pre=2):
    step = 1
    ans = step
    while step >= 10** -pre:
        while a ** ans < b:
            ans += step
            if a ** ans == b:
                return ans
        ans -= step
        step /= 10
    return ans     
        
a = int(input("輸入底數"))
b = int(input("輸入數值"))
print(f"{b}以{a}為底的對數:{myLog(a,b):.2f}")


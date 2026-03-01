def fact_iter(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    return result

def fact_rec(n):
    if n == 1:
        return 1
    else:
        return n * fact_rec(n-1)
    
n = int(input("請輸入階乘數:"))
print(f"{n}!={fact_iter(n)}")
print(f"{n}!={fact_rec(n)}")

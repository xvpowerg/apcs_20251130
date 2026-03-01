def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True
n = int(input("請輸入整數"))
if is_prime(n):
    print(f"{n}是質數")
else:
    print(f"{n}不是質數")
    
primeNums = []

for j in range(2,n+1):
    if is_prime(j):
        primeNums.append(j)
print(primeNums)        

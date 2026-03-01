import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

n = int(input("輸入一個正整數"))
if is_prime(n):
    print(f"{n}是質數")
else:
    print(f"{n}不是質數")
print(is_prime(n))

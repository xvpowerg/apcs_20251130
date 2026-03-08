def fib_loop(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    num1,num2 = 0,1
    nextNum = num1 + num2
    for i in range(2,n):
        num1 = num2
        num2 = nextNum
        nextNum = num1 + num2
    return nextNum
def fib_rec1(n,memo=None):
    if memo is None:
        memo = {}
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib_rec1(n-1,memo) + fib_rec1(n-2,memo)
    return memo[n]

#print(f"迴圈fib:{fib_loop(100)}")
print(f"遞迴fib:{fib_rec1(100)}")



s1 =0
for i in range(7):
    s1 += 3 + 5 * i
print(s1)    

def func1(x):
    if x == 1:
        return 3
    else:
        return func1(x-1) + 3+5*(x-1)
    
print(func1(7))    

s2 = 0
for k in range(10):
    s2 += 2*(-2)**k
print(s2)

def func2(y):
    if y == 1:
        return 2
    else:
        return func2(y-1) -(-2)**y
print(func2(10))    


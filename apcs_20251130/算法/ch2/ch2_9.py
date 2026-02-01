y = [i for i in range(1,11)]
print(y)
y = [x ** 2 for x in range(1,11)]
print(y)
y = [x+20 for x in range(1,11) if x % 2 != 0]
print(y)
celsius = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
y = [9/5 * x + 32 for x in celsius]
print(y)

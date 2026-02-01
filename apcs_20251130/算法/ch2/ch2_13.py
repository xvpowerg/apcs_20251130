poly1 = [1,-3,2]
x = 2
fx = 0
for i in range(len(poly1)):
    fx += poly1[i] * x ** i
print(f"fx({x})=",fx)
poly2 = [3,2,2,-3,1,1,0]

y = 2
fy = 0
for j in range(poly2[0]):
    fy += poly2[2 * j + 1] * y ** poly2[2*(j+1)]
print(f"fy({y})={fy}")    

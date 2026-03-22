numStr = input()
A, B = 0, 0
for i in range(len(numStr)):
    if i % 2 == 0:  
      B += int(numStr[i])# 偶數位
    else:
      A += int(numStr[i])# 奇數位
        
print(abs(A - B))

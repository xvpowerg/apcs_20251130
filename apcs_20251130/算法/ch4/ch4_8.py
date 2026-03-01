from itertools import permutations
from itertools import combinations
perm = permutations([1,2,3,4])
for i in list(perm):
    print(i)
print("==========")
com = combinations([1,2,3,4],3)
for i in list(com):
    print(i)

subjs = ['國語', '數學', '英文']
scores = [100, 80, 95]

print(list(zip(subjs,scores)))
for n,s in zip(subjs,scores):
    print(n,s)

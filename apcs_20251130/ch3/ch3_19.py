subjs = ['國語', '數學', '英文']
scores = [100, 80, 95]
myZip = []
for i in range(len(subjs)):
    data = (subjs[i],scores[i])
    myZip.append(data)    
print(myZip)

for sub,sco in myZip:
    print(sub,sco)

Sean,David,Amy = 0,1,2
Ch,En,Ma = 0,1,2
score = [[70,80,70],
         [60,55,70],
         [77,88,99]]

print("Sean:",score[Sean])
print("David:",score[David][Ma])
score.sort(key=sum)#用加總排序
for s in score:
    print(s)
sumList = []
for a1 in score:
    sum1 = 0
    for s in a1:
        sum1+=s        
    sumList.append(sum1)    
print(sumList)  

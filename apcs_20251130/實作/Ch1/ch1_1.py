#取得資料筆數 n
n = int(input())
#取得資料 inStrs, scores
inStrs = input().split()
scores = []
for i in range(n):
    scores.append(int(inStrs[i]))
#排序
scores.sort()
#搜尋最高不及格分數 highFail 及最低及格分數 lowPass
highFail, lowPass = 0,0
#scores[0] >= 60：highFail = 'best case', lowPass = scores[0]
if(scores[0]>=60):
    highFail = 'best case'
    lowPass = scores[0]
#scores[n-1] < 60：highFail = scores[n-1],  lowPass = 'worst case'
elif(scores[n-1]<60):
    highFail = scores[n-1]
    lowPass = 'worse case'
else:
    #i => 0 – n-2
    for i in range(n-1):
        highFail = scores[i]
        lowPass = scores[i+1]
        #lowPass >=60 中斷
        if(lowPass>=60):
            break
#列印結果
for s in scores:
    print(s, end=' ')
#print(' '.join(str(s) for s in scores))
print()
print(highFail)
print(lowPass)
    

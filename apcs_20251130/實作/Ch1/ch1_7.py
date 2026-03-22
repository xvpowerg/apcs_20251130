#讀取線段數量 n
n = int(input())

#讀取n次字串，切割組成線段起點及終點列表，加入 lines 二維列表
lines=[]
for i in range(n):
    pairs = input().split(' ')
    lines.append([int(pairs[0]), int(pairs[1])])

#將 lines 以線段起點排序
lines.sort(key=lambda x:x[0])
#print(lines)

#將線段合併處理為不重疊線段，加入resultLines二維列表
#以第一組線段(lines[0])作為當前線段curline
resultLines=[]
curline = lines[0]
#將lines[i] 由索引1-n 逐一取出
for i in range(1, n):
    #若當前線段與lines[i]沒有重疊，當前線段加入resultLines
    if(curline[1]<=lines[i][0]):
        resultLines.append(curline)
        curline = lines[i]
    #若當前線段與lines[i] 重疊且curline終點<lines[i]終點，合併線段
    elif(curline[1]<lines[i][1]):
        curline = [curline[0], lines[i][1]]
#將最後的當前線段加入resultLines
resultLines.append(curline)
#print(resultLines)

#輸出不重疊線段總長度
length = 0
for rLine in resultLines:
    length = length + (rLine[1]-rLine[0])

print(length)
        

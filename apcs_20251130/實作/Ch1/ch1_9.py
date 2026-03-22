#讀取資料 N M ：群 個
ins = list(map(int, input().split()))
N = ins[0]
M = ins[1]

#讀取N次，切割為M筆資料
#取得每一群中的最大值(索引0)，加入LNums集合
LNums = []
for i in range(N):
    row = list(map(int, input().split()))
    row.sort(reverse=True)
    LNums.append(row[0])

#LNums集合加總和為S
S = sum(LNums)

#LNums集合中可將S整除的數字加入RNums 集合
RNums = []
for l in LNums:
    if(S%l==0):
        RNums.append(l)
        
#輸出 S
print(S)

#最大值中可將S整除的數字(RNums 集合)
#無資料顯示-1
if(len(RNums)!=0):
    for r in RNums:
        print(r, end=' ')
    print()
else:
    print(-1)

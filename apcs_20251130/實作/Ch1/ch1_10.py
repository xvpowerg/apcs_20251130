direction=[[0,-1],[-1,0],[0,1],[1,0]]           #方向順序[左、上、右、下]
n = int(input())
d = int(input())                                #初始方向: 0代表左、1代表上、2代表右、3代表下

data=[]
for i in range(n):
    temp=[]
    temp=input().split()
    data.append(temp)

step = 1
stepcounter = 0
counter = 1
row = n // 2
col = n // 2
print("%d" %int(data[row][col]),end='')
while counter < n * n:
    for i in range(step):
        row += direction[d][0]
        col += direction[d][1]
        print("%d" %int(data[row][col]),end='')
        counter=counter+1
        if counter==n*n: # 超過最大數量跳出迴圈
            break
    if counter==n*n:# 超過最大數量跳出迴圈
        break
    stepcounter=stepcounter+1#步驟數量＋1
    if stepcounter % 2 == 0: #步驟數量 如是偶數就改變動作次數
        step=step+1
    d += 1 #切換到下一個動作
    d %= 4 #每四筆換到0

def h(data,no):                                 #計算節點的高度
    height=0                                    #記錄目前最大的高度,預設值為0
    if len(data[no]):
        for i in range(len(data[no])):
            temp=h(data,data[no][i])+1
            height = max(temp,height)
        return height;                          #傳回子節點最大的高度
    else:
        return 0                                #葉節點為遞迴函數的結束出口

n=int(input())                                  #n節點總數
data={}
for i in range(n):                              #輸入每列資料
    temp = input().split()
    subnode=int(temp[0])
    row=[]
    if subnode>0:                               #有子節點才輸入
        for j in range(1,subnode+1):
            row.append(int(temp[j]))
    data[i+1]=row
#print(data)

root, total, highest = 0, 0, 0
for i in range(1,n+1):                          #依序計算每一節點的最大高度
    high = h(data,i)                              #節點的最大高度
    if high > highest:                            #如果該節點高度大於目前最大高度
        highest = high                            #將 hi 設為目前最大高度
        root=i                                  #將該節點編號設為根節點編號
    total+=high                                 #累計所有節點的最大高度

print("%d" %root)                               #根節點編號
print("%d" %total)                              #所有節點最大高度總和

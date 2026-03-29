def dfsDistance(x):                                         #計算中間過程最大深度 
    global child, blood_distance
    if len(child[x]) == 0:                                  #沒有小孩是遞迴的出口條件
        return 0
    elif len(child[x])==1:                                  #只有一個子節點
        return dfsDistance(child[x][0])+1
    else:                                                   #2個子節點以上       
        max1, max2 = 0, 0                                   #走訪每個子節點，找出最大深度前兩名 max1, max2
        for ch in child[x]:                                 #逐一處理每一個子節點
            depth = dfsDistance(ch) + 1                     #取得此子節點最大深度
            if depth > max1:                                #此子節點
                max1, depth = depth, max1
            if depth > max2:
                max2 = depth
        blood_distance = max(blood_distance, max1+max2)#max1單一路最深 blood_distance 是左右兩分支
        return max1

N = int(input())
child = {}                                                  #血緣圖形
for i in range(N):                                          #字典儲存子節點資訊
    child[i] = []
    
for i in range(N-1):                                        #讀取N-1筆資料
    inStr = input()
    a,b = map(int, inStr.split())
    child[a].append(b)                                      #儲存各節點對應子節點資訊
   

root = list(range(N))
for i in child:
    for j in child[i]:                                      #節點不為其他節點之子節點為根節點
        root.remove(j)

blood_distance = 0                                          #最遠血緣關係
from_root = dfsDistance(root[0])                            #由根節點計算葉節點最大深度
blood_distance = max(from_root, blood_distance)             #與節點到兩個不同葉節點深度相加比較大小
print(blood_distance)

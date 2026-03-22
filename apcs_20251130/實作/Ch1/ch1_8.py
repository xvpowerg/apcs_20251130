N = int(input())                        #讀取總群體人數N
BF = list(map(int, input().split()))    #最好朋友字串，切割轉型後存入集合BF
#print(BF)

'''小群體G (二維List) 搜尋處理'''

G = []                                  #宣告列表G，包含多個集合LG
for i in range(N):                      #索引i由0-N，驗證i是否存在於已知LG中
    for LG in G:
        if(i in LG):                    #i存在於其中一個小群體:跳離迴圈
            break    
    else:                               #i不存在於目前小群體:建立newLG，索引i加入newLG
        newLG = []
        newLG.append(i)
        f = BF[i]                       # 取得好友 f = BF[i]

        while f != newLG[0]:            # f 不等於newLG[0]，索引 f 加入newLG
            newLG.append(f)           
            f = BF[f]                   # 取得下一個好友f = BF[f]，重複執行
            #print(newLG)
        G.append(newLG)                 # newLG 加入列表G
        
print(len(G))                           # 輸出G 中 LG 的組數
#print(G)

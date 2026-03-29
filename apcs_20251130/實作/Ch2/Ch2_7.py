'''測試K個基地台服務範圍為d時，
   是否可覆蓋所有服務點'''
def isCovered(d):
    global N, K, P
    nP =0
    count = 0
    pos = 0
    while pos<N:                                #從最前面開始取得服務點
        nP = P[pos] + d;                        #基地台的下一個涵蓋範圍
        count+=1                                #記錄基地台數目
        if count>K:                             #如果基地台數量已大於K,無法涵蓋,傳回False
            return False;                       
        if (P[N-1]<=nP) and (count<=K):         #如果涵蓋範圍包含全部,則傳回True
            return True;                        #在基地台數量未大於K時,最後一個基地台被涵蓋
        pos=pos+1
        while P[pos]<=nP:                       #尋找超過涵蓋範圍的基地台
            pos+=1                              #基地台仍在涵蓋範圍,pos遞增

N, K = map(int, input().split())                #服務點數目N, 基地台數目K
P = list(map(int, input().split()))             #服務點位置序列P
P.sort()                                        #服務點位置排序

mn = 1                                          #最小直徑
mx = (P[-1]-P[0])//K+1                          #最大直徑(最小與最大服務站距離)/基地台個數+1
                                                #答案介於這兩數之間，使用二元搜尋找出答案
while mn <= mx:
    mid = (mn + mx) // 2                        #二分搜尋中間直徑mid
    if(isCovered(mid)):                         #K 個基地台，能覆蓋 N 個服務點
        mx = mid                                #最大直徑改為mid
    else:
        mn = mid + 1                            #最小直徑改為mid+1
    if mn == mx:
        break
print("%d" %mx)

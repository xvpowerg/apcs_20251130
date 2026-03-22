def josephusLuckyPerson(ls, m, k):
    # ls: 目前還在圈內的人（list，內容是1~N號碼）
    # m: 每次數到第m個人淘汰
    # k: 只淘汰k次就停止（不一定要到剩一人）
    idx = 0  # 起始位置，第一回合從0號（也就是1號）開始
    for i in range(k):
        # 每次從idx往後數m-1個（因為包含自己）
        idx = (idx + m - 1) % len(ls)
        # 淘汰第idx個，從list移除
        ls.pop(idx)
        # 移除後idx已經指向淘汰者的下一位
        # 下次循環，炸彈就從這個人繼續數
    # 淘汰k次後，現在的idx正好指向「下一位」
    # 注意：這裡要對len(ls)取餘數，防止idx超過末端
    return ls[idx % len(ls)]

#----------------主程式----------------

# 讀取輸入字串，空白分割後分別轉成整數
inStrs = input().split(' ')
N = int(inStrs[0])  # 圈內人數
M = int(inStrs[1])  # 每次第M個淘汰
K = int(inStrs[2])  # 淘汰K次後就結束

# 建立1~N號碼的list
pList = [i for i in range(1, N + 1)]

# 呼叫函式得到幸運者編號
luckyPerson = josephusLuckyPerson(pList, M, K)
print(luckyPerson)  # 輸出幸運者

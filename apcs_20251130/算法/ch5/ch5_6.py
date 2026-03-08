def combine(lst,n):
    if len(lst) == n:
        return [lst]
    elif n == 1:
        return [[x] for x in lst]
    else:
        out = []
        #len(lst) - n因為要保證足夠n筆 +1因為range不包含n 假設n=3 len = 3 3-3 = 0 0+1 = 1
        #表示只能跑一次
        #如果 n=3 len=2 2-3 = -1 + 1 =0 表示不能跑 因為長度不夠n了
        for i in range(len(lst) - n + 1):
            first = lst[i]
            tails = combine(lst[i+1:],n-1)
            for c in tails:
                out.append([first]+c)
        return  out

myList = combine([1,2,3,4,5,6],4)
for v in myList:
    print(v)

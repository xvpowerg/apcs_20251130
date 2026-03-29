k = int(input())
a = input()
uorl = [] # 01 list
#將字母轉換成數字
for c in a:
 if c>='A' and c<='Z': uorl.append(0) 
 elif c>='a' and c<='z': uorl.append(1)
seg = []
my_len = 1
for i in range(1,len(uorl)):
    if uorl[i] == uorl[i -1]: #前後數字一樣相加
        my_len += 1
    else:
      seg.append(my_len)
      my_len = 1
seg.append(my_len)  
#print(seg)
longest = 0
m = len(seg)
le = 0
while le<m:
    while le < m and seg[le] != k: #找到連續k字串的開始
        le+=1
    if le >= m:break;
    ri = le + 1 #找到下一格數字是否為K
    while ri < m and seg[ri] == k:
        ri += 1
    t = (ri - le) * k   #算出長度*k 總長度4
    if le > 0 and seg[le-1] > k: #左邊大於k也算在長度內
        t+=k 
    if ri < m and seg[ri]  > k: #右邊大於k也算在長度內
        t += k
    if t > longest:longest = t #最大的交錯字串
    le = ri + 1 #找下一個看看
print(longest)     

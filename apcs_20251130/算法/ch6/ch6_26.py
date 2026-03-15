bottleType=(30,18,5,1)
def fill(amt):
    dp = [amt+1] * (amt + 1)
    dp[0] = 0    
    for i in range(1, amt + 1):
        temp = [dp[i]]
        for bottle in bottleType:
            if i >= bottle:
                temp.append(dp[i-bottle]+1)
        dp[i] = min(temp)
    #print(dp)
    return -1 if dp[-1] == amt + 1 else dp[-1]

count = 0
amount = int(input('輸入填充水量:'))
answer=fill(amount)
print('最少需使用%d個容器'%answer)

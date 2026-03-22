# 讀入要倒幾次飲料
n = int(input())

# 讀入杯子的四個參數
# w1 = 下半部正方形底面的邊長
# w2 = 上半部正方形底面的邊長
# h1 = 下半部高度
# h2 = 上半部高度
w1, w2, h1, h2 = map(int, input().split())

# 讀入每一次倒入的飲料體積
vs = list(map(int, input().split()))

# a1 = 下半部底面積
a1 = w1 * w1

# a2 = 上半部底面積
a2 = w2 * w2

# v1 = 下半部容量
# 容量 = 底面積 × 高度
v1 = a1 * h1

# v2 = 上半部容量
v2 = a2 * h2

# total = 整個杯子的總容量
total = v1 + v2


# 傳入目前總水量 water
# 回傳目前水位高度
def get_height(water):

    # 如果總水量還沒超過下半部容量 v1
    # 代表水還在下半部
    if water <= v1:
        return water // a1

    # 如果總水量超過下半部容量 v1
    # 但還沒超過整個杯子的總容量 total
    # 代表下半部已滿，剩下的水在上半部
    elif water <= total:
        return h1 + (water - v1) // a2

    # 如果超過整個杯子的總容量
    # 代表整個杯子已滿
    else:
        return h1 + h2


# now = 目前杯中的總水量
now = 0

# ans = 記錄最大的單次上升高度
ans = 0

# 依序處理每一次倒入的體積
for x in vs:
    # 倒之前的高度
    before = get_height(now)

    # 倒完之後的總水量
    # 如果超過杯子容量，就只算到滿杯
    now = min(now + x, total)

    # 倒之後的高度
    after = get_height(now)

    # 這次上升的高度
    rise = after - before

    # 更新最大值
    ans = max(ans, rise)

# 輸出答案
print(ans)

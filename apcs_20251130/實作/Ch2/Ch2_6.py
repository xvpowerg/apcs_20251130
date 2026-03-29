class Item:
    def __init__(self, w, f):
        self.w = w          # 這個物品的重量
        self.f = f          # 這個物品會被拿幾次

    def __lt__(self, other):
        # __lt__ 的意思是：
        # 當 sort() 排序時，要決定「誰應該排前面」
        #
        # 假設現在比的是兩個物品：
        # self 和 other
        #
        # 如果 self 放在上面，other 放在下面
        # 那麼之後拿 other 的時候，要先抬起 self
        # 這樣的花費是：self.w * other.f
        #
        # 如果 other 放在上面，self 放在下面
        # 那麼之後拿 self 的時候，要先抬起 other
        # 這樣的花費是：other.w * self.f
        #
        # 誰的花費比較小，誰就應該放上面
        #
        # 如果 self 放上面比較省，就回傳 True
        return self.w * other.f < other.w * self.f


items = []          # 用來放所有物品
min_energy = 0      # 最後的最小總耗能
total = 0           # 目前上面所有物品的總重量

N = int(input())                            # 讀入物品數量
weights = list(map(int, input().split()))   # 讀入每個物品的重量
frequent = list(map(int, input().split()))  # 讀入每個物品的取用次數

for i in range(N):
    # 把第 i 個物品包成一個 Item 物件
    # 裡面記住它的重量和取用次數
    items.append(Item(weights[i], frequent[i]))

# 排序：
# 會自動用上面寫好的 __lt__ 規則來排
# 排完後，前面的物品比較適合放上面
items.sort()

for item in items:
    # 現在輪到這個物品被處理
    #
    # 拿這個物品時，要先抬起它上面的全部物品
    # 上面總重量就是 total
    #
    # 而這個物品總共要拿 item.f 次
    # 所以它造成的耗能是：
    # 上方總重量 * 取用次數
    min_energy += total * item.f

    # 這個物品處理完後，
    # 對下面的物品來說，它也會變成「上面的重量之一」
    # 所以把它的重量加進 total
    total += item.w

# 印出答案
print(min_energy)

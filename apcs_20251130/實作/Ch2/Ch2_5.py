from collections import deque

n = int(input())                  # 節點總數

data = {}                         # data[i] = i 的子節點列表
parent = [0] * (n + 1)           # parent[i] = i 的父節點
child_count = [0] * (n + 1)      # child_count[i] = i 還有幾個子節點沒處理完
height = [0] * (n + 1)           # height[i] = i 的高度

# 讀資料
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    subnode = temp[0]            # 子節點個數
    row = []

    for j in range(1, subnode + 1):
        child = temp[j]
        row.append(child)
        parent[child] = i        # 記下 child 的爸爸是 i

    data[i] = row
    child_count[i] = subnode     # 一開始有幾個孩子

# 先把所有葉節點放進 queue
q = deque()
for i in range(1, n + 1):
    if child_count[i] == 0:
        q.append(i)              # 沒小孩，高度就是 0

# 從葉節點往上推高度
while q:
    node = q.popleft()
    p = parent[node]             # 找 node 的爸爸

    if p != 0:                   # 如果有爸爸
        height[p] = max(height[p], height[node] + 1)
        child_count[p] -= 1      # 表示爸爸有一個孩子處理完了

        # 如果爸爸的孩子都處理完，就可以進 queue
        if child_count[p] == 0:
            q.append(p)

# 找最大高度的節點編號
root = 1
highest = height[1]
total = height[1]

for i in range(2, n + 1):
    if height[i] > highest:
        highest = height[i]
        root = i
    total += height[i]

print(root)
print(total)

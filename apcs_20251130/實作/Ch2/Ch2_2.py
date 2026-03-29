from collections import deque

def bfs(start):
    dist = [-1] * n                     # dist[i] = start 到 i 的距離
    q = deque([start])
    dist[start] = 0

    far_node = start                    # 目前找到最遠的人
    far_dist = 0                        # 目前找到最遠距離

    while q:
        now = q.popleft()

        for nxt in graph[now]:
            if dist[nxt] == -1:         # 還沒走過
                dist[nxt] = dist[now] + 1
                q.append(nxt)

                if dist[nxt] > far_dist:
                    far_dist = dist[nxt]
                    far_node = nxt

    return far_node, far_dist


n = int(input())
graph = [[] for _ in range(n)]          # 無向圖

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)                  # 反方向也加上，因為要算任意兩人的距離

# 第一次 BFS：先找出某個最遠端點
far1, _ = bfs(0)

# 第二次 BFS：從最遠端點再找一次，得到真正答案
far2, answer = bfs(far1)

print(answer)

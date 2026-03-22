from collections import deque

N, M, K = map(int, input().split())
people = deque(range(1, N + 1))      # 建立1~N號的環形隊列

for _ in range(K):
    people.rotate(-(M - 1))          # 傳遞炸彈M-1次，讓第M個人到最前面
    people.popleft()                 # 淘汰最前面的人

print(people[0])                     # 淘汰K次後，隊首即為幸運者

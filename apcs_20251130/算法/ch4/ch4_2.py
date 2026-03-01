from collections import deque
q = deque([1,2,3,4,5])
q.append(6)
print(q)
q.rotate(2)#往右推
print(q)
q.rotate(-3)#往左推
print(q)
first = q.popleft()
print(first)
right = q.pop()
print(right)

print(q)


import collections

queue = collections.deque()
print(queue)

# 进队
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)

# 出队
res1 = queue.popleft()
print(queue)
res2 = queue.popleft()
print(queue)
res3 = queue.popleft()
print(queue)

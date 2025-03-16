

# 큐 구현

from collections import deque

queue = deque(['Eric', 'John', 'Michael'])
print(queue)
# deque(['Eric', 'John', 'Michael'])

print(queue.append("Terry")) # Terry arrives
# None

print(queue.append("Graham")) # Graham arrives
# None

print(queue.popleft()) # The first to arrive now leaves
# Eric

print(queue.popleft()) # The second to arrive now leaves
# John

print(queue) # Remaining queue in order of arrival
# deque(['Michael', 'Terry', 'Graham'])
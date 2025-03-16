


from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

heapify(data) # rearrange the list into heap order

heappush(data, -5)

print([heappop(data) for i in range(3)])
# [-5, 0, 1]
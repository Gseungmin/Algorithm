import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
ind = [0]*(N+1)
true = [0]*(N+1)
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    ind[b] += 1

import heapq
queue = []
for i in range(1,N+1):
    if ind[i] == 0:
        queue.append(i)
        true[i] = 1
queue.sort() 
while queue:
    x = heapq.heappop(queue)
    print(x, end = " ")
    for dx in graph[x]:
        if true[dx] == 0:
            ind[dx] -= 1
            if ind[dx] == 0:
                heapq.heappush(queue, dx)
                true[dx] = 1
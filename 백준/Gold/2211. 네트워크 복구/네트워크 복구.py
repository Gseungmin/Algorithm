import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    A, B, C = map(int,input().split())
    graph[A].append([B,C])
    graph[B].append([A,C])

import heapq
heap = []
INF = int(1e9)
heapq.heappush(heap,[0,1])
true = [False]*(N+1)
dist = [INF]*(N+1)
dist[1] = 0
prev = [0]*(N+1)
while heap:
    k, x = heapq.heappop(heap)
    if true[x] == True:
        continue
    true[x] = True
    for nx, c in graph[x]:
        if true[nx] == False:
            if dist[nx] > dist[x] + c:
                dist[nx] = dist[x] + c
                prev[nx] = x
                heapq.heappush(heap,[dist[nx], nx])

route = dict()
for i in range(2,N+1):
    x = i
    while x != 1:
        nx = prev[x]
        route[(min(x,nx), max(x,nx))] = True
        x = nx
print(len(route))
for i, j in route:
    print(i, j)
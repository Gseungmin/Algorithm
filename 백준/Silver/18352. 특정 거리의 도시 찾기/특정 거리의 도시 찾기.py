import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K, X = map(int,input().split())
dist = [INF]*(N+1)
cost = dict()
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    cost[(a,b)] = 1

import heapq
heap = []
true = [False]*(N+1)
dist[X] = 0
heapq.heappush(heap, [0,X])
while heap:
    t, x = heapq.heappop(heap)
    if true[x] == True:
        continue
    true[x] = True
    for nx in graph[x]:
        if true[nx] == False and dist[nx] > dist[x] + cost[(x,nx)]:
            dist[nx] = dist[x] + cost[(x,nx)]
            heapq.heappush(heap,[dist[nx], nx])

ans = []
for i in range(2,N+1):
    if dist[i] == K:
        ans.append(i)
if not ans:
    print(-1)
    sys.exit()
for i in ans:
    print(i)
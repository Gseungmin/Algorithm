import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int,input().split())
s = int(input())
cost = dict()
graph = [[] for i in range(N+1)]
true = [False]*(N+1)
dist = [INF]*(N+1)
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    if (a,b) in cost:
        cost[(a,b)] = min(cost[(a,b)], c)
    else:
        cost[(a,b)] = c
import heapq
heap = []
heapq.heappush(heap, [0,s])
dist[s] = 0
while heap:
    t, x = heapq.heappop(heap)
    if true[x] == True:
        continue
    true[x] = True
    for nx in graph[x]:
        if true[nx] == False and dist[nx] > dist[x] + cost[(x,nx)]:
            dist[nx] = dist[x] + cost[(x,nx)]
            heapq.heappush(heap, [dist[nx], nx])
for i in range(1,N+1):
    if dist[i] == INF:
        print("INF")
        continue
    print(dist[i])
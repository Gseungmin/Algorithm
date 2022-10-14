import sys
input = sys.stdin.readline
N, M, X = map(int,input().split())
INF = int(1e9)
graph = [[] for i in range(N+1)]
cost = dict()
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    cost[(a,b)] = c
import heapq

def Dijk(start, dist):
    dist[start] = 0
    heap = []
    true = [False]*(N+1)
    heapq.heappush(heap,[0,start])
    while heap:
        t, x = heapq.heappop(heap)
        if true[x] == True:
            continue
        true[x] = True
        for nx in graph[x]:
            if true[nx] == False and dist[nx] > dist[x] + cost[(x,nx)]:
                dist[nx] = dist[x] + cost[(x,nx)]
                heapq.heappush(heap,[dist[nx], nx])
    return

k = [INF]*(N+1)
Dijk(X, k)
ans = 0
for i in range(1,N+1):
    if i != X:
        dist = [INF]*(N+1)
        Dijk(i, dist)
        ans = max(ans, dist[X]+k[i])
print(ans)
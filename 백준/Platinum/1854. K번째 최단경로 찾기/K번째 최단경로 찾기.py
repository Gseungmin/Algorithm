import sys
input = sys.stdin.readline
import heapq
N, M, K = map(int,input().split())
INF = sys.maxsize
dist = [[]*(K+1) for i in range(N+1)]
heapq.heappush(dist[1],0)
heap = []
heapq.heappush(heap,[0,1])
true = [-1]*(N+1)
graph = [[] for i in range(N+1)]
cost = dict()
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    cost[(a,b)] = c
while heap:
    k, x = heapq.heappop(heap)
    for nx in graph[x]:
        if len(dist[nx])<K:
            heapq.heappush(dist[nx], -(k+cost[(x,nx)]))
            heapq.heappush(heap,[k+cost[(x,nx)], nx])
        elif len(dist[nx])==K:
            if dist[nx] and -dist[nx][0] > (k+cost[(x,nx)]):
                heapq.heappop(dist[nx])
                heapq.heappush(dist[nx], -(k+cost[(x,nx)]))
                heapq.heappush(heap,[k+cost[(x,nx)], nx])
for i in range(1,N+1):
    if K > len(dist[i]):
        print(-1)
    else:
        print(-dist[i][::-1][K-1])
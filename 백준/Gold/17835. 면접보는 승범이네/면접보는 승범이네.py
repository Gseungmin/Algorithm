import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
INF = sys.maxsize
cost = dict()
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int,input().split())
    if (b,a) not in cost:
        graph[b].append(a)
        cost[(b,a)] = c
    else:
        cost[(b,a)] = min(cost[(b,a)], c)
A = list(map(int,input().split()))
for i in A:
    graph[0].append(i)
    cost[(0,i)] = 0
import heapq
heap = []
heapq.heappush(heap,[0,0])
true = [False]*(N+1)
dist = [INF]*(N+1)
dist[0] = 0
while heap:
    t, x = heapq.heappop(heap)
    if true[x] == True:
        continue
    true[x] = True
    for nx in graph[x]:
        if true[nx] == False:
            if dist[nx] > dist[x] + cost[(x,nx)]:
                dist[nx] = dist[x] + cost[(x,nx)]
                heapq.heappush(heap,[dist[nx], nx])
Max = 0
for i in range(1,N+1):
    if dist[i] != INF:
        Max = max(Max, dist[i])
for i in range(1,N+1):
    if dist[i] == Max:
        print(i)
        print(dist[i])
        sys.exit()
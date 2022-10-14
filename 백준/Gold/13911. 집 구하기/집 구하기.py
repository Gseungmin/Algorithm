import sys
input = sys.stdin.readline

N, E = map(int,input().split())
graph = [[] for i in range(N+2)]
cost = dict()
for i in range(E):
    a, b, c = map(int,input().split())
    if (a,b) in cost:
        cost[(b,a)] = min(cost[(b,a)], c)
        cost[(a,b)] = min(cost[(a,b)], c)
    else:
        graph[a].append(b)
        graph[b].append(a)
        cost[(b,a)] = c
        cost[(a,b)] = c
M, x = map(int,input().split())
Mac = list(map(int,input().split()))
S, y = map(int,input().split())
Star = list(map(int,input().split()))
List = set(Mac+Star)
for i in Mac:
    graph[0].append(i)
    cost[(0,i)] = 0
for i in Star:
    graph[N+1].append(i)
    cost[(N+1,i)] = 0

import heapq
def Dijk(start, k, true, dist):
    heap = []
    dist[start] = 0
    heapq.heappush(heap,[0,start])
    while heap:
        t, x = heapq.heappop(heap)
        if true[x] == True:
            continue
        true[x] = True
        for nx in graph[x]:
            if true[nx] == False:
                if dist[nx] > dist[x]+cost[(x,nx)] and dist[x]+cost[(x,nx)] <= k:
                    dist[nx] = dist[x] + cost[(x,nx)]
                    heapq.heappush(heap,[dist[nx],nx])
    return

INF = int(1e9)
true1 = [False]*(N+2)
dist1 = [INF]*(N+2)
Dijk(0, x, true1, dist1)
true2 = [False]*(N+2)
dist2 = [INF]*(N+2)
Dijk(N+1, y, true2, dist2)
ans = INF
for i in range(1,N+1):
    if i in List:
        continue
    if true1[i] == True and true2[i] == True:
        if dist1[i] != INF and dist2[i] != INF:
            ans = min(ans, dist1[i]+dist2[i])
if ans == INF:
    print(-1)
else:
    print(ans)
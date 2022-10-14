import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
cost = dict()
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    if (a,b) in cost:
        cost[(a,b)] = min(cost[(a,b)],c)
    else:
        cost[(a,b)] = c
    if (b,a) in cost:
        cost[(b,a)] = min(cost[(b,a)],c)
    else:
        cost[(b,a)] = c
x1, x2 = map(int,input().split())

INF = int(1e9)
import heapq
def Dijk(start):
    heap = []
    true = [-1]*(N+1)
    dist = [INF]*(N+1)
    dist[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        t, x = heapq.heappop(heap)
        if true[x] == 1:
            continue
        true[x] = 1
        for nx in graph[x]:
            if true[nx] == -1:
                if dist[nx] > dist[x] + cost[(x,nx)]:
                    dist[nx] = dist[x] + cost[(x,nx)]
                    heapq.heappush(heap,(dist[nx],nx))
    return dist
dist1 = Dijk(1)
dist2 = Dijk(x1)
dist3 = Dijk(x2)
case1 = dist1[x1]+dist2[x2]+dist3[N]
case2 = dist1[x2]+dist3[x1]+dist2[N]
ans = min(case1, case2)
if ans >= INF:
    print(-1)
else:
    print(ans)
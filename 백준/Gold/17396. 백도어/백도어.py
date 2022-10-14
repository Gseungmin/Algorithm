import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int,input().split())
List = list(map(int,input().split()))
cost = dict()
graph = [[] for i in range(N)]
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    if (a,b) in cost:
        cost[(a,b)] = min(cost[(a,b)], c)
        cost[(b,a)] = min(cost[(b,a)], c)
    else:
        cost[(a,b)] = c
        cost[(b,a)] = c
List[-1] = 0
dist = [INF]*N
dist[0] = 0
true = [False]*N
import heapq
heap = []
heapq.heappush(heap,[0,0])
while heap:
    t, x = heapq.heappop(heap)
    if true[x] != False:
        continue
    true[x] = True
    for nx in graph[x]:
        if true[nx] == False and List[nx] == 0 and dist[nx] > dist[x] + cost[(x,nx)]:
            dist[nx] = dist[x] + cost[(x,nx)]
            heapq.heappush(heap,[dist[nx], nx])
if dist[N-1] == INF:
    print(-1)
else:
    print(dist[N-1])
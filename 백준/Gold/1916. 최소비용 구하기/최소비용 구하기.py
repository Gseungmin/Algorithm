import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
INF = int(1e9)
dist = [INF]*(N+1)
true = [False]*(N+1)
cost = dict()
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    if (a,b) in cost:
        cost[(a,b)] = min(cost[(a,b)], c)
    else:
        cost[(a,b)] = c
start, end = map(int,input().split())
import heapq
heap = []
heapq.heappush(heap,[0, start])
dist[start] = 0
while heap:
    c, x = heapq.heappop(heap)
    if true[x] != False:
        continue
    true[x] = True
    for nx in graph[x]:
        if true[nx] == False:
            if dist[nx] > dist[x] + cost[(x,nx)]:
                dist[nx] = dist[x] + cost[(x,nx)]
                heapq.heappush(heap, [dist[nx], nx])
print(dist[end])
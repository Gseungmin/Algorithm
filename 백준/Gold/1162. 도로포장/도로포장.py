import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M, K = map(int,input().split())
cost = dict()
graph = [[] for i in range(N+1)]
true = [[False]*(K+1) for i in range(N+1)]
dist = [[INF]*(K+1) for i in range(N+1)]
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    if (a,b) in cost:
        cost[(a,b)] = min(cost[(a,b)], c)
    else:
        cost[(a,b)] = c
    if (b,a) in cost:
        cost[(b,a)] = min(cost[(b,a)], c)
    else:
        cost[(b,a)] = c
import heapq
heap = []
heapq.heappush(heap, [0,0,1])
dist[1][0] = 0
while heap:
    t, k, x = heapq.heappop(heap)
    if true[x][k] == True:
        continue
    true[x][k] = True
    for nx in graph[x]:
        if k == K:
            if true[nx][k] == False and dist[nx][k] > dist[x][k] + cost[(x,nx)]:
                dist[nx][k] = dist[x][k] + cost[(x,nx)]
                heapq.heappush(heap, [dist[nx][k], k, nx])
        if k < K:
            if true[nx][k+1] == False and dist[nx][k+1] > dist[x][k]:
                dist[nx][k+1] = dist[x][k]
                heapq.heappush(heap, [dist[nx][k+1], k+1, nx])
            if true[nx][k] == False and dist[nx][k] > dist[x][k] + cost[(x,nx)]:
                dist[nx][k] = dist[x][k] + cost[(x,nx)]
                heapq.heappush(heap, [dist[nx][k], k, nx])
print(min(dist[N]))
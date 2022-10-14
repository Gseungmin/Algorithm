import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
INF = int(1e9)
dist = [INF]*(N+1)
true = [False]*(N+1)
prev = [-1]*(N+1)
cost = dict()
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    if (a,b) in cost:
        cost[(a,b)] = min(cost[(a,b)], c)
    else:
        cost[(a,b)] = c
start, e = map(int,input().split())
import heapq
heap = []
heapq.heappush(heap,[0, start])
dist[start] = 0
prev[start] = 0
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
                prev[nx] = x
print(dist[e])
ans = [e]
pre = prev[e]
while pre != 0:
    ans.append(pre)
    pre = prev[pre]
print(len(ans))
print(" ".join(map(str, ans[::-1])))
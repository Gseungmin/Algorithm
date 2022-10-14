import sys
input = sys.stdin.readline
N, M, K, S = map(int,input().split())
p, q = map(int,input().split())
zom = [int(input()) for i in range(K)]
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
def BFS():
    queue = deque()
    for i in zom:
        queue.append(i)
        true[i] = 0
    if S == 0:
        return
    while queue:
        x = queue.popleft()
        for nx in graph[x]:
            if true[nx] == -1:
                true[nx] = true[x] + 1
                if true[nx] == S:
                    continue
                queue.append(nx)
    return
true = [-1]*(N+1)
BFS()
import heapq
INF = sys.maxsize
check = [False]*(N+1)
dist = [INF]*(N+1)
dist[1] = 0
heap = []
heapq.heappush(heap,[0,1])
def Dijk():
    while heap:
        t, x = heapq.heappop(heap)
        if check[x] == True:
            continue
        check[x] = True
        for nx in graph[x]:
            if check[nx] == False:
                if true[nx] == -1:
                    if dist[nx] > dist[x] + p:
                        dist[nx] = dist[x] + p
                        heapq.heappush(heap,[dist[nx], nx])
                else:
                    if true[nx] != 0:
                        if dist[nx] > dist[x] + q:
                            dist[nx] = dist[x] + q
                            heapq.heappush(heap,[dist[nx], nx])
    return
Dijk()
if true[N] == -1:
    print(dist[N]-p)
else:
    print(dist[N]-q)
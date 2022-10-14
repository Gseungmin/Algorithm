import sys
input = sys.stdin.readline
import heapq
def Dijk(start):
    heap = []
    heapq.heappush(heap,[0,start])
    while heap:
        t, x = heapq.heappop(heap)
        if true[x] == True:
            continue
        true[x] = True
        for nx in graph[x]:
            if true[nx] == False and dist[nx] > dist[x] + cost[(x,nx)]:
                dist[nx] = dist[x] + cost[(x,nx)]
                heapq.heappush(heap,[dist[nx],nx])
    return

from collections import deque
def BFS():
    queue = deque()
    queue.append(E)
    while queue:
        nx = queue.popleft()
        if nx == S:
            continue
        for x in graph_r[nx]:
            if (dist[nx]-dist[x] == cost[(x,nx)]) and ((x,nx) not in visited) and (nx in graph[x]):
                graph[x].discard(nx)
                visited.add((x,nx))
                queue.append(x)
    return
while 1:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    S, E = map(int,input().split())
    graph = [set() for i in range(N)]
    graph_r = [set() for i in range(N)]
    cost = dict()
    INF = int(1e9)
    for i in range(M):
        a, b, c = map(int,input().split())
        graph[a].add(b)
        graph_r[b].add(a)
        cost[(a,b)] = c
    visited = set()
    dist = [INF]*N
    dist[S] = 0
    true = [False]*N
    Dijk(S)
    BFS()
    dist = [INF]*N
    dist[S] = 0
    true = [False]*N
    Dijk(S)
    if dist[E] == INF:
        print(-1)
    else:
        print(dist[E])
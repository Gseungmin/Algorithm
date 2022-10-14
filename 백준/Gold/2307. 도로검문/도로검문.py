import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [[] for i in range(N+1)]
cost = dict()
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    cost[(a,b)] = c
    cost[(b,a)] = c

import heapq
INF = int(1e9)
def Dijk(a,b,check):
    true = [False]*(N+1)
    heap = []
    heapq.heappush(heap,[0,0,1])
    dist = [INF]*(N+1)
    dist[1] = 0
    while heap:
        t, pr, x = heapq.heappop(heap)
        if true[x] == True:
            continue
        true[x] = True
        if check == 0:
            prev[x] = pr
        for nx in graph[x]:
            if a == x and b == nx:
                continue
            if b == x and a == nx:
                continue
            if true[nx] == False:
                if dist[nx] > dist[x] + cost[(x,nx)]:
                    dist[nx] = dist[x] + cost[(x,nx)]
                    heapq.heappush(heap,[dist[nx], x, nx])
    return dist[N]

prev = [0]*(N+1)
time = Dijk(0,0,0)
pr = N
ans = 0
while 1:
    k = Dijk(pr,prev[pr],1)
    if k == INF:
        print(-1)
        sys.exit()
    ans = max(ans,k-time)
    pr = prev[pr]
    if pr == 1:
        print(ans)
        break
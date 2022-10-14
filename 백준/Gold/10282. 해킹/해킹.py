import sys
input = sys.stdin.readline
t = int(input())
import heapq
INF = int(1e9)
for _ in range(t):
    N, D, C = map(int,input().split())
    graph = [[] for i in range(N+1)]
    cost = dict()
    for i in range(D):
        a, b, c = map(int,input().split())
        graph[b].append(a)
        cost[(b,a)] = c
    heap = []
    heapq.heappush(heap,[0,C])
    true = [False]*(N+1)
    dist = [INF]*(N+1)
    ans = 0
    cnt = 0
    dist[C] = 0
    while heap:
        k, x = heapq.heappop(heap)
        if true[x] == True:
            continue
        true[x] = True
        cnt += 1
        ans = max(ans,k)
        for nx in graph[x]:
            if true[nx] == False and dist[nx] > dist[x] + cost[(x,nx)]:
                dist[nx] = dist[x] + cost[(x,nx)]
                heapq.heappush(heap, [dist[nx], nx])
    print(cnt, ans)
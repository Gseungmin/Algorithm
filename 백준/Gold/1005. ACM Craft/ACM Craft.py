import sys
input = sys.stdin.readline
import heapq
t = int(input())
for _ in range(t):
    N, K = map(int,input().split())
    graph = [[] for i in range(N+1)]
    ind = [0]*(N+1)
    true = [False]*(N+1)
    cost = [0] + list(map(int,input().split()))
    for i in range(K):
        a, b = map(int,input().split())
        graph[a].append(b)
        ind[b] += 1
    E = int(input())
    heap = []
    for i in range(1,N+1):
        if ind[i] == 0:
            heapq.heappush(heap,[cost[i],i])
    ans = 0
    while heap:
        t, x = heapq.heappop(heap)
        ans += t
        if x == E:
            print(ans)
            break
        for i in heap:
            i[0] -= t
        for nx in graph[x]:
            if true[nx] == False:
                ind[nx] -= 1
                if ind[nx] == 0:
                    heapq.heappush(heap,[cost[nx],nx])
                    true[nx] = True
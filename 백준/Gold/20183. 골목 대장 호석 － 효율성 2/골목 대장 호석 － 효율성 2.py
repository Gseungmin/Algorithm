import sys
input = sys.stdin.readline
INF = int(1e14)+1
N, M, A, B, C = map(int,input().split())
graph = [[] for i in range(N+1)]
import heapq
Min_list = []
left = INF
right = 0
for i in range(M):
    x, y, z = map(int,input().split())
    graph[x].append([y,z])
    graph[y].append([x,z])
    left = min(left, z)
    right = max(right, z)

def Dijk(S, k):
    heap = []
    dist[S] = 0
    heapq.heappush(heap,[0,S])
    while heap:
        t, x = heapq.heappop(heap)
        if true[x] == True:
            continue
        true[x] = True
        for nx, t in graph[x]:
            if t > k:
                continue
            if true[nx] == False and dist[nx] > dist[x]+t:
                dist[nx] = dist[x]+t
                heapq.heappush(heap,[dist[nx], nx])
    return

ans = -1
while left <= right:
    mid = (left+right)//2
    true = [False]*(N+1)
    dist = [INF]*(N+1)
    Dijk(A, mid)
    if dist[B] <= C:
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)
import sys
input = sys.stdin.readline
import heapq
N, P, K = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(P):
    a, b, c = map(int,input().split())
    graph[b].append([a,c])
    graph[a].append([b,c])

INF = sys.maxsize
def Dijk(limit):
    dist = [INF]*(N+1)
    dist[1] = 0
    heap = []
    heapq.heappush(heap,[0,1])
    while heap:
        t, x = heapq.heappop(heap)
        if dist[x] < t:
            continue    
        for nx, c in graph[x]:
            if c > limit:
                if t+1 < dist[nx]:
                    dist[nx] = t+1
                    heapq.heappush(heap,[t+1,nx])
            else:
                if t < dist[nx]:
                    dist[nx] = t
                    heapq.heappush(heap,[t,nx])
    if dist[N] > K:
        return False
    return True
        
left = 0
right = 1000001
ans = -1
while left <= right: #이분 탐색을 통해 남은 것들의 가격중 제일 비싼 것
    mid = (left+right)//2
    if Dijk(mid) == True:
        right = mid-1
        ans = mid
    else:
        left = mid+1
print(ans)
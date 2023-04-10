import sys
input = sys.stdin.readline
import heapq
N, M = map(int,input().split())
cost = [0] + list(map(int,input().split())) #주유소 리터당 가격
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
heap = [] #비용, 최소 주유소, 위치
heapq.heappush(heap, [0,cost[1],1])

INF = int(1e9)
dist = [[INF]*(2501) for i in range(N+1)]
true = [[False]*(2501) for i in range(N+1)]
dist[1][cost[1]] = 0

while heap:
    c, k, x = heapq.heappop(heap)
    if true[x][k] == True:
        continue
    true[x][k] = True
    if x == N:
        print(c)
        sys.exit()
    for nx, d in graph[x]:
        value = min(cost[nx], k)
        if true[nx][value] == False:
            if dist[nx][value] > dist[x][k] + d*k: #d는 거리, k는 기름 최솟값
                dist[nx][value] = dist[x][k] + d*k
                heapq.heappush(heap, [dist[nx][value], value, nx])
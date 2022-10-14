import sys
input = sys.stdin.readline
import heapq
N = int(input())
T, M = map(int,input().split())
L = int(input())
graph = [[] for i in range(N+1)]
for i in range(L):
    x, y, time, cost = map(int,input().split())
    graph[x].append([y,time,cost])
    graph[y].append([x,time,cost])

INF = int(1e9)
def Dijk():
    heap = []
    heapq.heappush(heap,[0,0,1]) #cost, time, 위치
    cost = [[INF]*(T+1) for i in range(N+1)]
    cost[1][0] = 0
    visited = [[False]*(T+1) for i in range(N+1)]
    while heap:
        c, t, x = heapq.heappop(heap)
        if x == N:
            if c <= M:
                return c
            else:
                return -1
        if visited[x][t] == True:
            continue
        visited[x][t] = True
        for nx, time, money in graph[x]:
            m = t+time
            if m <= T and visited[nx][m] == False and c+money <= M:
                if cost[nx][m] > c + money:
                    cost[nx][m] = c + money
                    heapq.heappush(heap,[cost[nx][m], m, nx])
    return -1
print(Dijk())
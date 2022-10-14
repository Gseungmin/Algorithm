import sys
input = sys.stdin.readline
N = int(input())
A = [list(map(int,input().split())) for i in range(N)]
INF = int(1e9)
import heapq
heap = []
heapq.heappush(heap,[0,0,0])
true = [[False]*N for i in range(N)]
dist = [[INF]*N for i in range(N)]
dist[0][0] = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while heap:
    k, x, y = heapq.heappop(heap)
    if true[x][y] == True:
        continue
    true[x][y] = True
    if x == N-1 and y == N-1:
        print(dist[x][y])
        sys.exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N and true[nx][ny] == False:
            m = abs(A[x][y]-A[nx][ny])
            if dist[nx][ny] > max(k,m):
                dist[nx][ny] = max(k,m)
                heapq.heappush(heap,[dist[nx][ny], nx, ny])
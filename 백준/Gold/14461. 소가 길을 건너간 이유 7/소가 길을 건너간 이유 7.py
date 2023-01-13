import sys
input = sys.stdin.readline
import heapq
N, T = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

heap = []
#최소 시간, x좌표, y좌표, 건넌 횟수
heapq.heappush(heap, [0,0,0,0])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = sys.maxsize
true = [[[False]*3 for i in range(N)] for j in range(N)]
dist = [[[INF]*3 for i in range(N)] for j in range(N)]
dist[0][0][0] = 0
while heap:
    t, x, y, k = heapq.heappop(heap)
    if true[x][y][k] != False:
        continue
    true[x][y][k] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            if k < 2:
                if true[nx][ny][k+1] == False:
                    if dist[nx][ny][k+1] > dist[x][y][k] + T:
                        dist[nx][ny][k+1] = dist[x][y][k] + T
                        heapq.heappush(heap, [dist[nx][ny][k+1],nx,ny,k+1])
            else:
                if true[nx][ny][0] == False:
                    if dist[nx][ny][0] > dist[x][y][k] + T + graph[nx][ny]:
                        dist[nx][ny][0] = dist[x][y][k] + T + graph[nx][ny]
                        heapq.heappush(heap, [dist[nx][ny][0],nx,ny,0])
print(min(dist[N-1][N-1]))
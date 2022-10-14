import sys
input = sys.stdin.readline
N, M, T = map(int,input().split())
INF = sys.maxsize
graph = [list(map(int,input().split())) for i in range(N)]
from collections import deque
queue = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dist = [[[INF]*2 for i in range(M)] for j in range(N)]
if graph[0][0] == 2:
    dist[0][0][1] = 0
    queue.append([0,0,1])
elif graph[0][0] == 0:
    dist[0][0][0] = 0
    queue.append([0,0,0])
while queue:
    x, y, t = queue.popleft()
    if dist[x][y][t] == T:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if t == 0:
                if graph[nx][ny] == 0:
                    if dist[nx][ny][0] == INF:
                        dist[nx][ny][0] = dist[x][y][0] + 1
                        queue.append([nx,ny,0])
                if graph[nx][ny] == 2:
                    if dist[nx][ny][1] == INF:
                        dist[nx][ny][1] = dist[x][y][0] + 1
                        queue.append([nx,ny,1])
            if t == 1:
                if dist[nx][ny][1] == INF:
                    dist[nx][ny][1] = dist[x][y][1] + 1
                    queue.append([nx,ny,1])
if dist[N-1][M-1][0] == INF and dist[N-1][M-1][1] == INF:
    print("Fail")
else:
    print(min(dist[N-1][M-1][0],dist[N-1][M-1][1]))
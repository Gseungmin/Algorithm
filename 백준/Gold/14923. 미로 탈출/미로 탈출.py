import sys
input = sys.stdin.readline
N, M = map(int,input().split())
x, y = map(int,input().split())
x, y = x-1, y-1
ex, ey = map(int,input().split())
ex, ey = ex-1, ey-1
graph = [list(map(int,input().split())) for i in range(N)]
true = [[[False]*2 for i in range(M)] for j in range(N)]
INF = int(1e9)
dist = [[[INF]*2 for i in range(M)] for j in range(N)]
dist[x][y][0] = 0
true[x][y][0] = True
from collections import deque
queue = deque()
queue.append([x,y,0])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    a, b, c = queue.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if c == 0:
                if graph[nx][ny] == 0:
                    if true[nx][ny][0] == False:
                        true[nx][ny][0] = True
                        dist[nx][ny][0] = dist[a][b][0] + 1
                        queue.append([nx,ny,0])
                if graph[nx][ny] == 1:
                    if true[nx][ny][1] == False:
                        true[nx][ny][1] = True
                        dist[nx][ny][1] = dist[a][b][0] + 1
                        queue.append([nx,ny,1])
            if c == 1:
                if graph[nx][ny] == 0:
                    if true[nx][ny][1] == False:
                        true[nx][ny][1] = True
                        dist[nx][ny][1] = dist[a][b][1] + 1
                        queue.append([nx,ny,1])
if true[ex][ey][0] == False and true[ex][ey][1] == False:
    print(-1)
elif true[ex][ey][0] == False and true[ex][ey][1] == True:
    print(dist[ex][ey][1])
elif true[ex][ey][0] == True and true[ex][ey][1] == False:
    print(dist[ex][ey][0])
else:
    print(min(dist[ex][ey][0],dist[ex][ey][1]))
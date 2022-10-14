import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
H, W, sx, sy, fx, fy = map(int,input().split())
sx, sy, fx, fy = sx-1, sy-1, fx-1, fy-1

cost_r = dict()
for i in range(N):
    x1, y1 = i, 0
    x2, y2 = i, W-1
    Sum = sum(graph[i][0:W])
    cost_r[(x1,y1)] = Sum
    while y2 < M-1:
        Sum -= graph[x1][y1]
        y1 += 1
        y2 += 1
        Sum += graph[x2][y2]
        cost_r[(x1,y1)] = Sum

cost_v = dict()
for i in range(M):
    x1, y1 = 0, i
    x2, y2 = H-1, i
    Sum = 0
    for k in range(0,H):
        Sum += graph[k][i]
    cost_v[(x1,y1)] = Sum
    while x2 < N-1:
        Sum -= graph[x1][y1]
        x1 += 1
        x2 += 1
        Sum += graph[x2][y2]
        cost_v[(x1,y1)] = Sum

dx = [-1,1,0,0]
dy = [0,0,-1,1]
true = [[-1]*M for i in range(N)]
true[sx][sy] = 0
from collections import deque
queue = deque()
queue.append([sx,sy])
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx+H-1<N and 0<=ny+W-1<M and 0<=nx<N and 0<=ny<M:
            if true[nx][ny] == -1:
                if i == 1:
                    if cost_r[(nx+H-1,ny)] == 0:
                        true[nx][ny] = true[x][y] + 1
                        queue.append([nx,ny])
                if i == 0:
                    if cost_r[(nx,ny)] == 0:
                        true[nx][ny] = true[x][y] + 1
                        queue.append([nx,ny])
                if i == 2:
                    if cost_v[(nx,ny)] == 0:
                        true[nx][ny] = true[x][y] + 1
                        queue.append([nx,ny])
                if i == 3:
                    if cost_v[(nx,ny+W-1)] == 0:
                        true[nx][ny] = true[x][y] + 1
                        queue.append([nx,ny])
print(true[fx][fy])
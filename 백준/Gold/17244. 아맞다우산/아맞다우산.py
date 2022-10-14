import sys
input = sys.stdin.readline
M, N = map(int,input().split())
graph = [list(input().strip()) for i in range(N)]
from collections import deque
queue = deque()
arr = dict()
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "X":
            arr[(i,j)] = cnt
            cnt += 1
        elif graph[i][j] == "S":
            x, y = i, j
queue.append([x,y,0,0])
true = [[[False]*(1<<cnt) for i in range(M)] for j in range(N)]
true[x][y][0] = True
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    x, y, cnt, dist = queue.popleft()
    if graph[x][y] == "E" and cnt == 2**(len(arr))-1:
        print(dist)
        sys.exit()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M and graph[nx][ny] != "#":
            if graph[nx][ny] == "X":
                nc = cnt|(1<<arr[(nx,ny)])
                if true[nx][ny][nc] == False:
                    true[nx][ny][nc] = True
                    queue.append([nx,ny,nc,dist+1])
            else:
                if true[nx][ny][cnt] == False:
                    queue.append([nx,ny,cnt,dist+1])
                    true[nx][ny][cnt] = True
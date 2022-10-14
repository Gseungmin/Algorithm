graph = [list(input()) for i in range(8)]
from collections import deque
queue = deque()
queue.append([7,0,0])
true = [[[-1]*9 for i in range(8)] for j in range(8)] #true[i][j][k] = k초일때 i,j이다.
dx = [-1,1,0,0,-1,-1,1,1,0]
dy = [0,0,1,-1,1,-1,1,-1,0]
true[7][0][0] = 0
while queue:
    x, y, t = queue.popleft()
    if x == 0 and y == 7:
        print(1)
        exit()
    for i in range(9):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<8 and 0<=ny<8:
            if t >= 8:
                if true[nx][ny][t] == -1:
                    true[nx][ny][t] = true[x][y][t] + 1
                    queue.append([nx,ny,t])
            else:
                if nx-t >= 0:
                    if graph[nx-t][ny] != "#":
                        if nx-t-1 >= 0:
                            if graph[nx-t-1][ny] != "#" and true[nx][ny][t+1] == -1:
                                true[nx][ny][t+1] = true[x][y][t] + 1
                                queue.append([nx,ny,t+1])
                        else:
                            if true[nx][ny][t+1] == -1:
                                true[nx][ny][t+1] = true[x][y][t] + 1
                                queue.append([nx,ny,t+1])
                else:
                    if true[nx][ny][t+1] == -1:
                        true[nx][ny][t+1] = true[x][y][t] + 1
                        queue.append([nx,ny,t+1])
print(0)
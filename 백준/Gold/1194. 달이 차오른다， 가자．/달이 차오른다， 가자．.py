import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(input().strip()) for i in range(N)]
true = [[[False]*64 for i in range(M)] for j in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == "0":
            graph[i][j] = "."
            x, y = i, j
            break
from collections import deque
queue = deque()
queue.append([x,y,0,0])
true[x][y][0] = True
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    x, y, c, cnt = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] == ".":
                if true[nx][ny][c] == False:
                    queue.append([nx,ny,c,cnt+1])
                    true[nx][ny][c] = True
            elif graph[nx][ny] == "1":
                print(cnt+1)
                sys.exit()
            else:
                if graph[nx][ny].isupper():
                    if c&1<<(ord(graph[nx][ny])-65):
                        if true[nx][ny][c] == False:
                            queue.append([nx,ny,c,cnt+1])
                            true[nx][ny][c] = True
                elif graph[nx][ny].islower():
                    nc = c|1<<(ord(graph[nx][ny])-97)
                    if true[nx][ny][nc] == False:
                        queue.append([nx,ny,nc,cnt+1])
                        true[nx][ny][nc] = True
print(-1)
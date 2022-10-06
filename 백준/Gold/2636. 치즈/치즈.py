import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
    
ans = 0
time = 0
while 1:
    out = deque()
    true = [[0]*M for i in range(N)]
    for i in range(N):
        if i == 0 or i == N-1:
            for j in range(M):
                out.append([i,j])
                true[i][j] = 1
        else:
            out.append([i,0])
            out.append([i,M-1])
            true[i][0] = 1
            true[i][M-1] = 1
    delete = set()
    while out:
        x, y = out.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if true[nx][ny] == 0:
                    if graph[nx][ny] == 0:
                        out.append([nx,ny])
                        true[nx][ny] = 1
                    elif graph[nx][ny] == 1:
                        delete.add((nx,ny))
    for x, y in delete:
        graph[x][y] = 0
    if len(delete) == 0:
        print(time)
        print(ans)
        break
    time += 1
    ans = len(delete)
import sys
input = sys.stdin.readline
import copy
N, M, T = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
clear = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == -1:
            clear.append([i,j])
cx1, cy1 = clear[0][0], clear[0][1]
cx2, cy2 = clear[1][0], clear[1][1]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while T > 0:
    Dust = [[0]*M for i in range(N)]
    for x in range(N):
        for y in range(M):
            if graph[x][y] == -1:
                Dust[x][y] = -1
            if graph[x][y] > 0:
                cnt = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny] != -1:
                            Dust[nx][ny] += graph[x][y]//5
                            cnt += 1
                Dust[x][y] += graph[x][y]-(graph[x][y]//5)*cnt
    for x in range(cx1-1,-1,-1):
        nx = x+1
        if nx == cx1:
            Dust[x][0] = 0
        else:
            Dust[nx][0] = Dust[x][0]
            Dust[x][0] = 0
    for y in range(1,M):
        ny = y-1
        if Dust[0][ny] == -1:
            Dust[0][y] = 0
        else:
            Dust[0][ny] = Dust[0][y]
            Dust[0][y] = 0
    for x in range(1,cx1+1):
        nx = x-1
        Dust[nx][M-1] = Dust[x][M-1]
        Dust[x][M-1] = 0
    for y in range(M-2,0,-1):
        ny = y+1
        Dust[cx1][ny] = Dust[cx1][y]
        Dust[cx1][y] = 0
        
    for x in range(cx2+1,N):
        nx = x-1
        if nx == cx2:
            Dust[x][0] = 0
        else:
            Dust[nx][0] = Dust[x][0]
            Dust[x][0] = 0
    for y in range(1,M):
        ny = y-1
        if Dust[N-1][ny] == -1:
            Dust[N-1][y] = 0
        else:
            Dust[N-1][ny] = Dust[N-1][y]
            Dust[N-1][y] = 0
    for x in range(N-2,cx2-1,-1):
        nx = x+1
        Dust[nx][M-1] = Dust[x][M-1]
        Dust[x][M-1] = 0
    for y in range(M-2,0,-1):
        ny = y+1
        Dust[cx2][ny] = Dust[cx2][y]
        Dust[cx2][y] = 0
    graph = copy.deepcopy(Dust)
    T -= 1
ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] > 0:
            ans += graph[i][j]
print(ans)
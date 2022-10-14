import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
time = 0
while cnt < 2:
    true = [[False]*M for i in range(N)]
    Dict = dict()
    k = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and true[i][j] == False:
                k += 1
                if k == 2:
                    print(time)
                    sys.exit()
                true[i][j] = True
                queue = deque()
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    l = 0
                    for m in range(4):
                        nx, ny = x+dx[m], y+dy[m]
                        if 0<=nx<N and 0<=ny<M:
                            if graph[nx][ny] == 0:
                                l += 1
                            if graph[nx][ny] != 0 and true[nx][ny] == False:
                                true[nx][ny] = True
                                queue.append([nx,ny])
                    Dict[(x,y)] = l
    if k == 0:
        print(0)
        sys.exit()
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                graph[i][j] = max(0, graph[i][j]-Dict[(i,j)])
    time += 1
print(0)
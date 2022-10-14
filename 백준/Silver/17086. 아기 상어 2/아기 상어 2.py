import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,1,-1,-1,1,-1,1]
ans = []
from collections import deque
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            true = [[-1]*M for k in range(N)]
            queue = deque()
            queue.append([i,j])
            true[i][j] = 0
            check = 0
            while queue:
                x, y = queue.popleft()
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny] == 1:
                            if true[nx][ny] == -1:
                                check = 1
                                ans.append(true[x][y]+1)
                                break
                        if true[nx][ny] == -1:
                            true[nx][ny] = true[x][y] + 1
                            queue.append([nx,ny])
                if check == 1:
                    break
if not ans:
    print(0)
    sys.exit()
print(max(ans))
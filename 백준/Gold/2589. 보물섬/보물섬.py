N, M = map(int,input().split())
graph = [list(input()) for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
from collections import deque
ans = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            true = [[-1]*M for k in range(N)]
            true[i][j] = 0
            queue = deque()
            queue.append([i,j])
            Max = 0
            while queue:
                x, y = queue.popleft()
                Max = max(Max, true[x][y])
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if true[nx][ny] == -1 and graph[nx][ny] == "L":
                            queue.append([nx,ny])
                            true[nx][ny] = true[x][y] + 1
            ans = max(ans, Max)
print(ans)
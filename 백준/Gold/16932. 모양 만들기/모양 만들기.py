import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
true = [[-1]*M for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]
from collections import deque
queue = deque()
size = []
group = 0
Set = set()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and true[i][j] == -1:
            cnt = 0
            queue.append([i,j])
            true[i][j] = group
            while queue:
                x, y = queue.popleft()
                cnt += 1
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if graph[nx][ny] == 1 and true[nx][ny] == -1:
                            true[nx][ny] = group
                            queue.append([nx,ny])
            Set.add(group)
            group += 1
            size.append(cnt)

Max = max(size)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            All = set()
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0<=x<N and 0<=y<M:
                    if graph[x][y] == 1 and true[x][y] in Set:
                        All.add(true[x][y])
            Sum = 0
            for k in All:
                Sum += size[k]
            Max = max(Max, Sum+1)
print(Max)
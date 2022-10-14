import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
index = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            index.append([i,j])
import itertools
virus = list(itertools.combinations(index,M))
from collections import deque
for case in virus:
    queue = deque()
    true = [[-1]*N for i in range(N)]
    for i in case:
        a, b = i
        queue.append([a,b])
        true[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<N and 0<=ny<N:
                if true[nx][ny] == -1:
                    if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                        queue.append([nx,ny])
                        true[nx][ny] = true[x][y] + 1
    Max = 0
    check = 0
    for i in range(N):
        for j in range(N):
            if true[i][j] == -1 and graph[i][j] != 1:
                check = 1
                break
            if true[i][j] != -1 and graph[i][j] == 0:
                Max = max(Max, true[i][j])
        if check == 1:
            break
    if check == 0:
        ans.append(Max)
if not ans:
    print(-1)
else:
    print(min(ans))
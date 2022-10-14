import sys
input = sys.stdin.readline
from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
ans = 1
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for h in range(1,100):
    true = [[0]*N for l in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and true[i][j] == 0:
                cnt += 1
                queue = deque()
                queue.append([i,j])
                true[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<N and 0<=ny<N:
                            if graph[nx][ny] > h and true[nx][ny] == 0:
                                true[nx][ny] = 1
                                queue.append([nx,ny])
    ans = max(ans, cnt)
print(ans)
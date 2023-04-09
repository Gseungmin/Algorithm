import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

true = [[False]*M for i in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            if true[i][j] == False:
                cnt += 1
                true[i][j] = True
                queue = deque()
                queue.append([i,j])
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        
                        #x 재정의
                        if nx == N:
                            nx = 0
                        if nx == -1:
                            nx = N-1
                        
                        #y 재정의
                        if ny == M:
                            ny = 0
                        if ny == -1:
                            ny = M-1
                        
                        if graph[nx][ny] == 0 and true[nx][ny] == False:
                            queue.append([nx,ny])
                            true[nx][ny] = True

print(cnt)
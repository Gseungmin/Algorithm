import sys
input = sys.stdin.readline
K = int(input())
M, N = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
true = [[[-1]*(K+1) for i in range(M)] for j in range(N)]

if M == 1 and N == 1:
    print(0)
    sys.exit()

dx = [-1,1,0,0,-1,-2,-2,-1,1,2,2,1]
dy = [0,0,1,-1,-2,-1,1,2,-2,-1,1,2]
from collections import deque
queue = deque()
queue.append([0,0,0])
true[0][0][0] = 0
while queue:
    x, y, z = queue.popleft()
    if x == N-1 and y == M-1:
        print(true[x][y][z])
        sys.exit()
    for i in range(12):
        if i == 4 and z == K:
            break
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if i <= 3:
                if graph[nx][ny] == 0 and true[nx][ny][z] == -1:
                    true[nx][ny][z] = true[x][y][z] + 1
                    queue.append([nx,ny,z])
            else:
                if graph[nx][ny] == 0 and true[nx][ny][z+1] == -1:
                    true[nx][ny][z+1] = true[x][y][z] + 1
                    queue.append([nx,ny,z+1])
print(-1)
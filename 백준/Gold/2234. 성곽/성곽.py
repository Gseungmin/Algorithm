import sys
input = sys.stdin.readline

def wall(num):
    value = 8
    List = [0]*4
    while 1:
        if num == 0:
            break
        if num >= 8:
            List[2] = 1
            num -= 8
        elif num >= 4:
            List[1] = 1
            num -= 4  
        elif num >= 2:
            List[0] = 1
            num -= 2
        elif num >= 1:
            List[3] = 1
            num -= 1
    return List

M, N = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
true = [[-1]*M for i in range(N)]
wall_graph = [[wall(graph[i][j]) for j in range(M)] for i in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
from collections import deque
group = 0
size = []
for i in range(N):
    for j in range(M):
        if true[i][j] == -1:
            queue = deque()
            queue.append([i,j])
            true[i][j] = group
            cnt = 1
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    if wall_graph[x][y][k] == 1:
                        continue
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<M:
                        if true[nx][ny] == -1:
                            cnt += 1
                            true[nx][ny] = group
                            queue.append([nx,ny])
            size.append(cnt)
            group += 1
print(group)
print(max(size))

Max = 0
for x in range(N):
    for y in range(M):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<N and 0<=ny<M:
                if true[nx][ny] != true[x][y]:
                    Max = max(Max, size[true[nx][ny]]+size[true[x][y]])
print(Max)
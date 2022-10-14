import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
from collections import deque
def BFS1(graph, N, x, y, dx, dy, true, num):
    queue = deque()
    queue.append([x,y])
    true[x][y] = 0
    graph[x][y] = num
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if true[nx][ny] == -1 and graph[nx][ny] == 1:
                    true[nx][ny] = 0
                    graph[nx][ny] = num
                    queue.append([nx,ny])
    return

true = [[-1]*N for i in range(N)]
num = 1
for i in range(N):
    for j in range(N):
        if true[i][j] == -1 and graph[i][j] == 1:
            BFS1(graph, N, i, j, dx, dy, true, num)
            num += 1

queue = deque()
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            queue.append([i,j])

def BFS2(graph, N, x, y, dx, dy, true, ans):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<N:
            if true[nx][ny] == -1 and graph[nx][ny] == 0:
                queue.append([nx,ny])
                true[nx][ny] = true[x][y] + 1
                graph[nx][ny] = graph[x][y]
            if graph[nx][ny] != 0 and graph[nx][ny] != graph[x][y]:
                ans.append(true[nx][ny]+true[x][y])
                return
    return
ans = []
while queue:
    x, y = queue.popleft()
    BFS2(graph, N, x, y, dx, dy, true, ans)
print(min(ans))
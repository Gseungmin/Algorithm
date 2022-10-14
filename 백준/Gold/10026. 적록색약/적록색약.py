N = int(input())
graph = [list(input()) for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
from collections import deque
def BFS(graph,x,y,dx,dy,true,word):
    queue = deque()
    true[x][y] = 1
    if word == 'G':
        graph[x][y] = 'R'
    queue.append([x,y])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<N:
                if true[nx][ny] == 0 and graph[nx][ny] == word:
                    true[nx][ny] = 1
                    queue.append([nx,ny])
                    if graph[nx][ny] == 'G':
                        graph[nx][ny] = 'R'
    return

check = 0
true = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if true[i][j] == 0:
            BFS(graph,i,j,dx,dy,true,graph[i][j])
            check += 1

check2 = 0
true = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if true[i][j] == 0:
            BFS(graph,i,j,dx,dy,true,graph[i][j])
            check2 += 1

print(check, end = " ")
print(check2)
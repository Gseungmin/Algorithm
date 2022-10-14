N, M = map(int,input().split())
graph = [list(input()) for i in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def water(graph, N, M, x, y, dx, dy, w_true, w_queue):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if w_true[nx][ny] == -1 and graph[nx][ny] != 'D' and graph[nx][ny] != 'X':
                w_true[nx][ny] = w_true[x][y] + 1
                w_queue.append([nx,ny])
    return
from collections import deque
w_queue = deque()
w_true = [[-1]*M for i in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == '*': #물의 위치라면
            w_queue.append([i,j])
            w_true[i][j] = 0
while w_queue:
    x, y = w_queue.popleft()
    water(graph, N, M, x, y, dx, dy, w_true, w_queue)
    
def BFS(graph, N, M, x, y, t, f_x, f_y, dx, dy, w_true, true):
    queue = deque()
    queue.append([x,y,t])
    while queue:
        a, b, t = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if true[nx][ny] == 0:
                    if nx == f_x and ny == f_y:
                        return t+1
                    if w_true[nx][ny] == -1 and graph[nx][ny] != 'X':
                        queue.append([nx,ny,t+1])
                        true[nx][ny] = 1
                    elif graph[nx][ny] != 'X' and t - w_true[nx][ny] < 0:
                        if (t+1) - w_true[nx][ny] < 0:
                            queue.append([nx,ny,t+1])
                            true[nx][ny] = 1
    return -1
            
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'D': #비버의 굴이라면
            f_x, f_y = i, j
        if graph[i][j] == 'S': #고슴도치의 위치라면
            x, y = i, j
true = [[0]*M for i in range(N)]
ans = BFS(graph, N, M, x, y, 0, f_x, f_y, dx, dy, w_true, true)
if ans == -1:
    print('KAKTUS')
else:
    print(ans)
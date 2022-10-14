import itertools
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def BFS(a,b,dx,dy,N,M,graph,dist):
    queue = deque()
    true = [[-1]*M for i in range(N)]
    queue.append([a,b])
    true[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 'x':
                    continue
                if true[nx][ny] == -1:
                    true[nx][ny] = true[x][y] + 1
                    queue.append([nx,ny])
                    if graph[nx][ny] == '*':
                        dist[a][b][nx][ny] = true[nx][ny]
    return
while 1:
    ans = []
    M, N = map(int,input().split())
    if M == 0 and N == 0:
        exit()
    graph = [list(input()) for i in range(N)]
    dirty = []
    dist = [[[[-1]*20 for i in range(20)] for j in range(20)] for k in range(20)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == '*':
                dirty.append([i,j])
                BFS(i,j,dx,dy,N,M,graph,dist)
            if graph[i][j] == 'o':
                BFS(i,j,dx,dy,N,M,graph,dist)
                x, y = i, j
    if not dirty:
        print(0)
        continue
    Dirty = list(itertools.permutations(dirty))
    check = 0
    for case in Dirty:
        cnt = dist[x][y][case[0][0]][case[0][1]]
        if cnt == -1:
            print(-1)
            check = 1
            break
        for k in range(len(case)-1):
            if dist[case[k][0]][case[k][1]][case[k+1][0]][case[k+1][1]] == -1:
                print(-1)
                check = 1
                break
            cnt += dist[case[k][0]][case[k][1]][case[k+1][0]][case[k+1][1]]
        if check == 1:
            break
        ans.append(cnt)
    if check == 1:
        continue
    print(min(ans))
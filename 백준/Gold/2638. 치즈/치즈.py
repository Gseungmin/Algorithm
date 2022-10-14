import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
ans = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while 1:
    #init bfs setting for cheeze that can be deleted
    cheeze = dict()
    queue = deque()
    true = [[0]*M for i in range(N)]
    for i in range(N):
        if i == 0 or i == N-1:
            for j in range(M):
                queue.append([i,j])
                true[i][j] = 1
        else:
            queue.append([i,0])
            queue.append([i,M-1])
            true[i][0] = 1
            true[i][M-1] = 1
        
    #finding cheeze that can be deleted
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if graph[nx][ny] == 1: #cheeze
                    if true[nx][ny] == 0: #not visit
                        true[nx][ny] = 1
                    elif true[nx][ny] == 1: #visit
                        cheeze[(nx,ny)] = 1
                else: #not cheeze
                    if true[nx][ny] == 0:
                        queue.append([nx,ny])
                        true[nx][ny] = 1
    
    #if no cheeze, then break
    if len(cheeze) == 0:
        print(ans)
        break
    else:
        ans += 1
    
    #delete cheeze
    for x,y in cheeze:
        graph[x][y] = 0
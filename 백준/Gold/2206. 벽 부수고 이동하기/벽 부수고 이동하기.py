from collections import deque
N, M = map(int,input().split())
graph = [list(map(int,list(input()))) for i in range(N)] #2차원 그래프
dist = [[[0]*2 for i in range(M)] for j in range(N)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def wall(graph, x1, y1, x2, y2, dist):
    queue = deque()
    queue.append([x1,y1,0])
    dist[x1][y1][0] = 1 #0,0,0을 방문 x와 y는 0이고 아직 벽을 부수지 않은 경우
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:  
                if dist[nx][ny][z] == 0 and graph[nx][ny] == 0: #(nx,ny) 벽이 아니고 방문하지 않았다면
                    dist[nx][ny][z] = dist[x][y][z] + 1
                    queue.append([nx,ny,z])
                if z == 0 and graph[nx][ny] == 1 and dist[nx][ny][z+1] == 0: #(nx,ny)가 벽이고 아직 벽을 한번도 방문하지 않았으며 아직 방문하지 않은 곳이라면
                    dist[nx][ny][z+1] = dist[x][y][z] + 1
                    queue.append([nx,ny,z+1])
    return

wall(graph, 0, 0, N-1, M-1, dist)
if dist[N-1][M-1][0] != 0 and dist[N-1][M-1][1] != 0:
    print(min(dist[N-1][M-1][0],dist[N-1][M-1][1]))
elif dist[N-1][M-1][0] != 0:
    print(dist[N-1][M-1][0])
elif dist[N-1][M-1][1] != 0:
    print(dist[N-1][M-1][1])
else:
    print(-1)
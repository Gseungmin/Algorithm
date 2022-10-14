import sys
input = sys.stdin.readline
INF = int(1e9)

def BF():
    dist[0][0] = 0
    for i in range(N*M):
        for j in edge:
            x1, y1, x2, y2, t = j[0][0], j[0][1], j[1][0], j[1][1], j[2]
            if dist[x1][y1] != INF and dist[x2][y2] > dist[x1][y1] + t:
                dist[x2][y2] = dist[x1][y1] + t
                if i == (N*M)-1:
                    return False
    return True

while 1:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    graph = [[0]*M for i in range(N)]
    G = int(input())
    for i in range(G):
        a, b = map(int,input().split())
        graph[a][b] = 1
    E = int(input())
    Dict = dict()
    for i in range(E):
        x1, y1, x2, y2, t = map(int,input().split())
        graph[x1][y1] = 2
        Dict[(x1,y1)] = (x2,y2,t)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    edge = []
    dist = [[INF]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if i == N-1 and j == M-1:
                continue
            if graph[i][j] == 1:
                continue
            if graph[i][j] == 2:
                a, b, c = Dict[(i,j)]
                edge.append([[i,j],[a,b],c])
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<M:
                    if graph[nx][ny] != 1:
                        edge.append([[i,j],[nx,ny],1])
    ans = BF()
    if ans == False:
        print("Never")
    else:
        if dist[N-1][M-1] == INF:
            print("Impossible")
        else:
            print(dist[N-1][M-1])
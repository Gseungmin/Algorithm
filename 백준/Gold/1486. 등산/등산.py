alpha = dict()
num = 0
for i in range(65,91):
    alpha[chr(i)] = num
    num += 1
for i in range(97,123):
    alpha[chr(i)] = num
    num += 1
N, M, T, D = map(int,input().split())
graph = [list(input()) for i in range(N)]
for i in range(N):
    for j in range(M):
        graph[i][j] = alpha[graph[i][j]]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)
import heapq
def Dijk(heap,true,dist,a,b):
    heapq.heappush(heap,[0,a,b])
    dist[a][b] = 0
    while heap:
        t,x,y = heapq.heappop(heap)
        if true[x][y] == True:
            continue
        true[x][y] = True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if true[nx][ny] == False:
                    if abs(graph[x][y]-graph[nx][ny]) <= T:
                        if graph[x][y] >= graph[nx][ny]:
                            if dist[nx][ny] > dist[x][y] + 1 and dist[x][y]+1 <= D:
                                dist[nx][ny] = dist[x][y]+1
                                heapq.heappush(heap,[dist[nx][ny],nx,ny])
                        else:
                            k = abs(graph[nx][ny]-graph[x][y])**2
                            if dist[nx][ny] > dist[x][y]+k and dist[x][y]+k <= D:
                                dist[nx][ny] = dist[x][y]+k
                                heapq.heappush(heap,[dist[nx][ny],nx,ny])
heap = []
true = [[False]*M for i in range(N)]
dist = [[INF]*M for i in range(N)]
Dijk(heap,true,dist,0,0)
Max = 0
for i in range(N):
    for j in range(M):
        if true[i][j] == True:
            r_heap = []
            r_true = [[False]*M for i in range(N)]
            r_dist = [[INF]*M for i in range(N)]
            Dijk(r_heap, r_true, r_dist, i, j)
            if r_true[0][0] == True and r_dist[0][0] + dist[i][j] <= D:
                Max = max(Max, graph[i][j])
print(Max)
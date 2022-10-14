N, M = map(int,input().split())
graph = []
true = []
dist = []
for i in range(N):
    graph.append(list(input()))
    true.append([0]*M)
    dist.append([0]*M)
true.append([0])

def ABS(num):
    if num < 0:
        num = -num
    return num
def DFS(Graph, x, y, dx, dy, true, dist):
    true[x][y] = 1
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if (((0<=a) and (a<N)) and ((0<=b) and (b<M))):
            if (true[a][b] == 0) and (Graph[a][b] == Graph[x][y]):
                dist[a][b] = dist[x][y] + 1
                DFS(Graph, a, b, dx, dy, true, dist)
            if (true[a][b] == 1) and (Graph[a][b] == Graph[x][y]) and (ABS(dist[a][b] - dist[x][y]) >= 3):
                true[N][0] = 1
                return
    return

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    for j in range(M):
        DFS(graph, i, j, dx, dy, true, dist)
        if true[N][0] == 1:
            break
    if true[N][0] == 1:
        break
if true[N][0] == 1:
    print('Yes')
else:
    print('No')
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
INF = int(1e9)
dist = [[INF]*N for i in range(N)]
dist2 = [[INF]*N for i in range(N)]
for i in range(M):
    u,v,k = map(int,input().split())
    u, v = u-1, v-1
    if k == 0:
        dist[u][v] = 0
        dist[v][u] = 1
    else:
        dist[u][v] = 0
        dist[v][u] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
K = int(input())
for _ in range(K):
    a, b = map(int,input().split())
    a, b = a-1, b-1
    if a == b:
        print(0)
        continue
    print(dist[a][b])
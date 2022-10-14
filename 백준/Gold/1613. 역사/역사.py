import sys
input = sys.stdin.readline
N, K = map(int,input().split())
graph = [[] for i in range(N+1)]
INF = int(1e9)
dist = [[INF]*(N) for i in range(N)]
for i in range(K):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)
    dist[a-1][b-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
M = int(input())
for i in range(M):
    a, b = map(int,input().split())
    if dist[a-1][b-1] == INF and dist[b-1][a-1] == INF:
        print(0)
    if dist[a-1][b-1] != INF:
        print(-1)
    if dist[b-1][a-1] != INF:
        print(1)
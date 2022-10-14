import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
INF = int(1e9)
dist = [[INF]*(N) for i in range(N)]
for i in range(M):
    a, b, c = map(int,input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
for i in range(N):
    for j in range(N):
        if i == j or dist[i][j] == INF:
            print(0, end = " ")
        else:
            print(dist[i][j], end = " ")
    print()
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
cost = dict()
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

ans = INF
for i in range(N):
    for j in range(N):
        if dist[i][j] != INF and dist[j][i] != INF:
            ans = min(ans, dist[i][j]+dist[j][i])
if ans != INF:
    print(ans)
else:
    print(-1)
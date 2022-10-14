import sys
input = sys.stdin.readline
N, M, K = map(int,input().split())
Item = list(map(int,input().split()))
INF = int(1e9)
dist = [[INF]*N for i in range(N)]
for i in range(K):
    a, b, c = map(int,input().split())
    dist[a-1][b-1] = c
    dist[b-1][a-1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
ans = 0
for i in range(N):
    Sum = Item[i]
    for j in range(N):
        if i == j:
            continue
        if dist[i][j] <= M:
            Sum += Item[j]
    ans = max(ans, Sum)
print(ans)
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int,input().split())
dist = [[INF]*N for i in range(N)]
for i in range(M):
    a, b, c = map(int,input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1],c)
    dist[b-1][a-1] = min(dist[b-1][a-1],c)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or k == j:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
J, S = map(int,input().split())
ans = -1
k = 0
Dict = dict()
Min = INF
for i in range(N):
    if i == J-1 or i == S-1:
        continue
    Min = min(Min, dist[i][J-1]+dist[i][S-1])
if Min == INF:
    print(-1)
    sys.exit()
for i in range(N):
    if i == J-1 or i == S-1:
        continue
    if dist[i][J-1] + dist[i][S-1] != Min:
        continue
    if dist[i][J-1] > dist[i][S-1]:
        continue
    if ans == -1:
        ans = i+1
        k = dist[i][J-1]
    else:
        if k > dist[i][J-1]:
            ans = i+1
            k = dist[i][J-1]
        elif k == dist[i][J-1]:
            if ans > i+1:
                ans = i+1
print(ans)
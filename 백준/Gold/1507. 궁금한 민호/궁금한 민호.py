import sys
input = sys.stdin.readline
N = int(input())
dist = []
INF = int(sys.maxsize)
for i in range(N):
    dist.append(list(map(int,input().split())))
    dist[i][i] = INF

Set = set()
for i in range(N):
    for j in range(N):
        if i != j:
            if (j,i) not in Set:
                Set.add((i,j))

for k in range(N):
    for i in range(N):
        if i == k:
            continue
        for j in range(N):
            if i == j or j == k:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                sys.exit()
            if dist[i][j] == dist[i][k] + dist[k][j]:
                Set.discard((i,j))
ans = 0
for i, j in Set:
    ans += dist[i][j]
print(ans)
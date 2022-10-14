INF = int(1e9)
N = int(input())
dist = [list(input()) for i in range(N)]
for i in range(N):
    for j in range(N):
        if dist[i][j] == "N":
            dist[i][j] = INF
        else:
            dist[i][j] = 1
            
ans = [0]*(N)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if dist[i][j] != INF:
            ans[i] += 1
Set = set()
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if i == k or j == k:
                continue
            if (dist[i][k] != INF and dist[j][k] != INF) and dist[i][j] == INF and (i,j) not in Set:
                ans[i] += 1
                Set.add((i,j))
print(max(ans))
N = int(input())
INF = int(1e9)
w1 = []
w2 = []
for i in range(N):
    w1.append(list(input()))
for i in range(N):
    w2.append(list(input()))
for i in range(N):
    for j in range(N):
        if w1[i][j] == ".":
            w1[i][j] = [INF, INF]
        else:
            w1[i][j] = [int(w1[i][j]), int(w2[i][j])]
dist = w1
for t in range(2):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if (dist[i][j][0]*dist[i][j][1]) > dist[i][k][0]*dist[i][k][1] + dist[i][k][0]*dist[k][j][1] + dist[k][j][0]*dist[i][k][1] + dist[k][j][0]*dist[k][j][1]:
                    dist[i][j][0] = dist[i][k][0] + dist[k][j][0]
                    dist[i][j][1] = dist[i][k][1] + dist[k][j][1]
ans = dist[0][1][0]*dist[0][1][1]
if ans >= INF:
    print(-1)
else:
    print(ans)
import sys
input = sys.stdin.readline
N = int(input())
dist = [list(map(int,input().split())) for i in range(N)]
INF = int(1e9)
for i in range(N):
    for j in range(N):
        if dist[i][j] == 0:
            dist[i][j] = INF

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(N):
    for j in range(N):
        if dist[i][j] == INF:
            print(0, end = " ")
        else:
            print(1, end = " ")
    print()
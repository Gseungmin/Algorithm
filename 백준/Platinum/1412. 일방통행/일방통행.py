INF = int(1e9)
N = int(input())
List = [list(input()) for i in range(N)]
import heapq
edge = []
dist = [[INF]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if List[i][j] == "Y" and List[j][i] == "N":
            dist[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(N):
    if dist[i][i] != INF:
        print("NO")
        exit()
print("YES")
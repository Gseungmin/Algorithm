import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    INF = int(1e9)
    N = int(input())
    List = [list(map(int,input().split())) for i in range(N+2)]
    dist = [[INF]*(N+2) for i in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            if i == j:
                continue
            x1, y1 = List[i]
            x2, y2 = List[j]
            k = abs(x1-x2)+abs(y1-y2)
            if k <= 1000:
                dist[i][j] = abs(x1-x2)+abs(y1-y2)
    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    if dist[0][N+1] != INF:
        print("happy")
    else:
        print("sad")
import sys
input = sys.stdin.readline
INF = int(1e9)
T = int(input())
import heapq
for _ in range(T):
    N, M = map(int,input().split())
    dist = [[INF]*N for i in range(N)]
    for i in range(M):
        a, b, c = map(int,input().split())
        dist[a-1][b-1] = c
        dist[b-1][a-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k]+dist[k][j]
    K = int(input())
    friends = list(map(int,input().split()))
    ans = []
    for i in range(N):
        value = 0
        for friend in friends:
            if friend-1 == i:
                continue
            value += dist[friend-1][i]
        heapq.heappush(ans,[value, i+1])
    print(heapq.heappop(ans)[1])
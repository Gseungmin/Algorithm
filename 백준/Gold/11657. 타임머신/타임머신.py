import sys
input = sys.stdin.readline
INF = sys.maxsize

def BF(start):
    dist[start] = 0
    for i in range(N):
        for j in edge:
            x, y, k = j[0], j[1], j[2]
            if dist[x] != INF and dist[y] > dist[x] + k:
                dist[y] = dist[x] + k
                if i == N-1:
                    return False
    return True

N, M = map(int,input().split())
edge = []
for i in range(M):
    a, b, c = map(int,input().split())
    edge.append([a,b,c])
dist = [INF]*(N+1)
ans = BF(1)
if not ans:
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
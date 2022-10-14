import sys
input = sys.stdin.readline
N, M = map(int,input().split())
dist = [[False]*N for i in range(N)]
for i in range(M):
    a, b = map(int,input().split())
    dist[b-1][a-1] = True
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][k] == True and dist[k][j] == True:
                dist[i][j] = True
less = dict()
more = dict()
for i in range(1,N+1):
    less[i] = 0
    more[i] = 0
for i in range(N):
    for j in range(N):
        if dist[i][j] == True:
            more[i+1] += 1
            less[j+1] += 1
cnt = set()
for i in range(1,N+1):
    if more[i] > N//2:
        cnt.add(i)
    if less[i] > N//2:
        cnt.add(i)
print(len(cnt))
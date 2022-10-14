import sys
input = sys.stdin.readline

N,M,X,Y = map(int,input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dp = [set() for i in range(Y+1)]
dp[0].add(X)
size = 1
while size <= Y:
    for x in dp[size-1]:
        for nx in graph[x]:
            if nx not in dp[size]:
                dp[size].add(nx)
    size += 1
dp[Y] = list(dp[Y])
dp[Y].sort()
if dp[Y]:
    print(" ".join(map(str,dp[Y])))
else:
    print(-1)
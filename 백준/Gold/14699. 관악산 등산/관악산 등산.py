import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int,input().split())
height = [0] + list(map(int,input().split()))
graph = [[] for i in range(N+1)]
true = dict()
for i in range(M):
    a, b = map(int,input().split())
    if height[a] < height[b]:
        if (a,b) not in true:
            graph[a].append(b)
            true[(a,b)] = True
    if height[a] > height[b]:
        if (b,a) not in true:
            graph[b].append(a)
            true[(b,a)] = True

dp = [0]*(N+1)
def DP(x, prev):
    if len(graph[x]) == 0:
        dp[x] = 1
        return 1
    if dp[x] != 0:
        return dp[x]
    k = 0
    for nx in graph[x]:
        k = max(k, DP(nx, x))
    dp[x] = 1+k
    return dp[x]

for i in range(1,N+1):
    DP(i,-1)
for i in range(1,N+1):
    print(dp[i])
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0]*2 for i in range(N+1)]
def DP(x, prev):
    if len(graph[x]) == 1 and x != 1:
        dp[x][1] = 1
        return
    dp[x][1] = 1
    for nx in graph[x]:
        if nx == prev:
            continue
        DP(nx, x)
        dp[x][1] += min(dp[nx][0], dp[nx][1])
        dp[x][0] += dp[nx][1]
    return

DP(1,-1)
Min = int(1e9)
for i in range(2):
    if dp[1][i] != 0:
        Min = min(Min, dp[1][i])
print(Min)
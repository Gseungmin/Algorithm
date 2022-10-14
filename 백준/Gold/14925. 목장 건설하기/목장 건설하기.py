import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [[0]*(n+1)]
for _ in range(m):
    graph.append([0]+list(map(int, input().split())))

dp = [[0]*(n+1)]
for _ in range(m):
    dp.append([0] + [0]*n)

ans = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if graph[i][j]==0:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            ans = max(ans, dp[i][j])

print(ans)
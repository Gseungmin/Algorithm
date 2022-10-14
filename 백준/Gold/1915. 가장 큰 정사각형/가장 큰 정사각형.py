N, M = map(int, input().split())
graph = [list(map(int,list(input()))) for i in range(N)]
dp = [[0]*(M+1) for j in range(N+1)]
side = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if graph[i-1][j-1] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            if dp[i][j] > side:
                side = dp[i][j]
print(side**2)
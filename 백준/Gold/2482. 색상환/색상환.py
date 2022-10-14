import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
Mod = 1000000003
dp = [[[[0]*2 for k in range(N)] for i in range(2)] for j in range(N)]
dp[0][1][1][1] = 1
for i in range(1,N):
    dp[i][1][1][0] = 1
for i in range(1,N):
    for j in range(1,N):
        dp[i][1][j][0] += dp[i-1][0][j-1][0]
        dp[i][1][j][1] += dp[i-1][0][j-1][1]
        dp[i][0][j][0] += dp[i-1][1][j][0] + dp[i-1][0][j][0]
        dp[i][0][j][1] += dp[i-1][1][j][1] + dp[i-1][0][j][1]
        dp[i][1][j][0] %= Mod
        dp[i][1][j][1] %= Mod
        dp[i][0][j][0] %= Mod
        dp[i][0][j][1] %= Mod
ans = (dp[N-1][1][K][0]+dp[N-1][0][K][1]+dp[N-1][0][K][0])%Mod
print(ans)
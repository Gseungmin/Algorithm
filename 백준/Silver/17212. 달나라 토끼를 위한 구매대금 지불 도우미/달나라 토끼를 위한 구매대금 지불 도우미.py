import sys
input = sys.stdin.readline
N = int(input())
INF = int(1e9)
ans = INF
dp = [INF]*(N+1)
dp[0] = 0
for i in range(1,N+1):
    if i == 1 or i == 2 or i == 5 or i == 7:
        dp[i] = 1
    if i+1 <= N:
        dp[i+1] = min(dp[i+1], dp[i]+1)
    if i+2 <= N:
        dp[i+2] = min(dp[i+2], dp[i]+1)
    if i+5 <= N:
        dp[i+5] = min(dp[i+5], dp[i]+1)
    if i+7 <= N:
        dp[i+7] = min(dp[i+7], dp[i]+1)
print(dp[N])
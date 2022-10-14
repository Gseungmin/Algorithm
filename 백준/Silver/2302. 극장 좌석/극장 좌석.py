import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
true = set()
for i in range(M):
    a = int(input())
    true.add(a-1)
dp = [[0]*2 for i in range(N)]
dp[0][0] = 1
for i in range(1,N):
    if i in true:
        dp[i][0] = dp[i-1][0]+dp[i-1][1]
    else:
        if i-1 in true:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
print(sum(dp[N-1]))
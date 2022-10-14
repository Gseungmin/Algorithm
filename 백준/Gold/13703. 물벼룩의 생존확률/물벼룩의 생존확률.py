import sys
input = sys.stdin.readline
K, N = map(int,input().split())
if K == 0:
    print(0)
    sys.exit()
dp = [[0]*(K+N+1) for i in range(N+1)]
dp[0][K] = 1
for i in range(1,N+1):
    for j in range(1,K+N+1):
        if j+1 < K+N+1:
            if dp[i-1][j+1] != 0:
                dp[i][j] += dp[i-1][j+1]
        if j-1 > 0:
            if dp[i-1][j-1] != 0:
                dp[i][j] += dp[i-1][j-1]
ans = 0
for i in range(K+N+1):
    ans += dp[N][i]
print(ans)
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
dp = [[[-1]*10001 for j in range(2)] for k in range(N)]
dp[0][0][0] = 0
dp[0][1][C[0]] = A[0]
for i in range(N-1):
    for j in range(10001):
        if dp[i][0][j] != -1:
            dp[i+1][0][j] = max(dp[i+1][0][j], dp[i][0][j])
            if dp[i][0][j] < M:
                dp[i+1][1][j+C[i+1]] = max(dp[i+1][1][j+C[i+1]], dp[i][0][j]+A[i+1])
        if dp[i][1][j] != -1:
            dp[i+1][0][j] = max(dp[i+1][0][j], dp[i][1][j])
            if dp[i][1][j] < M:
                dp[i+1][1][j+C[i+1]] = max(dp[i+1][1][j+C[i+1]], dp[i][1][j]+A[i+1])
        
INF = sys.maxsize
ans = INF
for i in range(N):
    for j in range(2):
        for k in range(10001):
            if dp[i][j][k] >= M:
                ans = min(ans, k)
print(ans)
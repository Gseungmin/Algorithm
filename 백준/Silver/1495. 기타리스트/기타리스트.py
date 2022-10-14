import sys
input = sys.stdin.readline
N, S, M = map(int,input().split())
V = [-1] + list(map(int,input().split()))
dp = [[-1]*(M+1) for i in range(N+1)]
dp[0][S] = 1
for i in range(1,N+1):
    for j in range(M+1):
        if j+V[i] <= M:
            if dp[i-1][j+V[i]] != -1:
                dp[i][j] = 1
        if j-V[i] >= 0:
            if dp[i-1][j-V[i]] != -1:
                dp[i][j] = 1
Max = -1
for i in range(M,-1,-1):
    if dp[N][i] != -1:
        print(i)
        sys.exit()
print(Max)
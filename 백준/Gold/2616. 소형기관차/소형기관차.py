import sys
input = sys.stdin.readline
N = int(input())
train = list(map(int,input().split()))
Sum = [0]*N
k = 0
for i in range(N):
    k += train[i]
    Sum[i] = k
M = int(input())
dp = [[[0]*2 for j in range(N)] for i in range(3)]
for i in range(M-1,N):
    if i == M-1:
        dp[0][i][1] = Sum[i]
    else:
        dp[0][i][1] = Sum[i]-Sum[i-M]
        dp[0][i][0] = max(dp[0][i-1][0], dp[0][i-1][1])
for i in range(2*M-1,N):
    if i == 2*M-1:
        dp[1][i][1] = Sum[i]
    else:
        dp[1][i][1] = Sum[i]-Sum[i-M]+max(dp[0][i-M][0], dp[0][i-M][1])
        dp[1][i][0] = max(dp[1][i-1][0], dp[1][i-1][1])
        
for i in range(3*M-1,N):
    if i == 3*M-1:
        dp[2][i][1] = Sum[i]
    else:
        dp[2][i][1] = Sum[i]-Sum[i-M]+max(dp[1][i-M][0], dp[1][i-M][1])
        dp[2][i][0] = max(dp[2][i-1][0], dp[2][i-1][1])
print(max(dp[2][N-1]))
import sys
input = sys.stdin.readline
dp = [[0]*10 for i in range(64)]
for i in range(10):
    dp[0][i] = 1
for k in range(1,64):
    for i in range(10):
        for j in range(i+1):
            dp[k][i] += dp[k-1][j]
T = int(input())
for i in range(T):
    a = int(input())
    print(sum(dp[a-1]))
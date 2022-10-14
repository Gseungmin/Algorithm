import sys
input = sys.stdin.readline
N = int(input())
if N <= 3:
    print(N)
    sys.exit()
dp = [0]*(N+1)
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, N+1):
    dp[i] = dp[i-1]+1
    mul = 2
    for j in range(i-3,0,-1):
        dp[i] = max(dp[i], dp[j]*mul)
        mul += 1
print(dp[-1])
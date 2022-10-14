import sys
input = sys.stdin.readline
dp = [0]*(5001)
dp[0] = 1
dp[2] = 1
for i in range(4,5001):
    for j in range(2,i+1,2):
        dp[i] += (dp[j-2]*dp[i-j])%1000000007
N = int(input())
for i in range(N):
    k = int(input())
    print(dp[k]%1000000007)
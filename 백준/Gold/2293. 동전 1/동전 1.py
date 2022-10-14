import sys
input = sys.stdin.readline
N, K = map(int,input().split())
value = [int(input()) for i in range(N)]
value.sort()
dp = [0]*(K+1)
for i in value:
    if i > K:
        continue
    dp[i] += 1
    for j in range(1,K+1):
        if j-i>=1:
            if dp[j-i] != 0:
                dp[j] += dp[j-i]
print(dp[K])
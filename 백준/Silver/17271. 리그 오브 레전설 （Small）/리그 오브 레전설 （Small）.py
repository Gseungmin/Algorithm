import sys
input = sys.stdin.readline
N, M = map(int,input().split())
if N < M:
    print(1)
    sys.exit()
if N == M:
    print(2)
    sys.exit()
dp = [0]*(N+1)
for i in range(1,M):
    dp[i] = 1
dp[M] = 2
for i in range(M+1,N+1):
    dp[i] = (dp[i-1]+dp[i-M]) % 1000000007
print(dp[N])
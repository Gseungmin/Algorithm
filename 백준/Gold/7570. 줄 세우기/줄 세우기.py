import sys
input = sys.stdin.readline
N = int(input())
child = list(map(int,input().split()))

dp = [0]*(N+1)
L = 0

for i in range(N):
    x = child[i]
    dp[x] = dp[x-1] + 1
    L = max(dp[x], L)

print(N-L)
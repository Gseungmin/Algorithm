import sys
input = sys.stdin.readline
N = int(input())
graph = list(map(int,input().split()))
dp = [-1]*N
dp[0] = 0
for i in range(N):
    if dp[i] == -1:
        continue
    for j in range(1,graph[i]+1):
        k = i+j
        if k >= N:
            break
        if dp[k] == -1:
            dp[k] = dp[i] + 1
        else:
            dp[k] = min(dp[k], dp[i]+1)
print(dp[N-1])
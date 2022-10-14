import sys
input = sys.stdin.readline
N = int(input())
List = [0] + [int(input()) for i in range(N)]
dp = [[-1]*2 for i in range(N+1)]
dp[0][0] = 0
for i in range(N):
    if i == 0:
        if i+1 <= N:
            dp[i+1][0] = List[i+1]
        if i+2 <= N:
            dp[i+2][0] = List[i+2]
        continue
    if dp[i][0] != -1:
        if i+1 <= N:
            dp[i+1][1] = max(dp[i+1][1],dp[i][0]+List[i+1])
        if i+2 <= N:
            dp[i+2][0] = max(dp[i+2][0],dp[i][0]+List[i+2])
    if dp[i][1] != -1:
        if i+2 <= N:
            dp[i+2][0] = max(dp[i+2][0],dp[i][1]+List[i+2])
print(max(dp[N]))
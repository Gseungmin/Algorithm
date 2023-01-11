import sys
input = sys.stdin.readline
N = int(input())
List = [0] + [int(input()) for i in range(N)]

dp = [[0]*(N+1) for j in range(N+1)]
dp[1][1] = List[1]
dp[1][0] = List[N]
for i in range(1,N):
    for j in range(N+1):
        if dp[i][j] != 0:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + List[j+1]*(i+1)) #앞은 선택한 경우
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + List[N+1-(i+1-j)]*(i+1))
print(max(dp[N]))
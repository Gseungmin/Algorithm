import sys
input = sys.stdin.readline
N, T = map(int,input().split())
List = [list(map(int,input().split())) for i in range(N)]
dp = [[[0]*2 for i in range(T+1)] for j in range(N)]
if List[0][0] <= T:
    dp[0][List[0][0]][1] = List[0][1]
for i in range(1,N):
    for j in range(T+1):
        if j-List[i][0] >= 0:
            dp[i][j][1] = max(dp[i-1][j-List[i][0]][0], dp[i-1][j-List[i][0]][1]) + List[i][1]
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])
ans = 0
for i in range(T+1):
    for j in range(2):
        ans = max(ans, dp[N-1][i][j])
print(ans)
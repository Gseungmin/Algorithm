import sys
input = sys.stdin.readline
N, M = map(int,input().split())
List = [int(input()) for i in range(N)]
dp = [[[-1]*3 for i in range(M+1)] for j in range(N)]
if List[0] == 1:
    dp[0][0][1] = 1
    dp[0][1][2] = 0
else:
    dp[0][0][1] = 0
    dp[0][1][2] = 1
    
for i in range(N-1):
    for j in range(M+1):
        if dp[i][j][1] != -1:
            if List[i+1] == 1:
                dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1]+1)
                if j+1 <= M:
                    dp[i+1][j+1][2] = max(dp[i+1][j+1][2], dp[i][j][1])
            else:
                dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1])
                if j+1 <= M:
                    dp[i+1][j+1][2] = max(dp[i+1][j+1][2], dp[i][j][1]+1)
        if dp[i][j][2] != -1:
            if List[i+1] == 1:
                dp[i+1][j][2] = max(dp[i+1][j][2], dp[i][j][2])
                if j+1 <= M:
                    dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][2]+1)
            else:
                dp[i+1][j][2] = max(dp[i+1][j][2], dp[i][j][2]+1)
                if j+1 <= M:
                    dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][2])
ans = 0
for k in range(N):
    for i in range(M+1):
        for j in range(1,3):
            ans = max(ans, dp[k][i][j])
print(ans)
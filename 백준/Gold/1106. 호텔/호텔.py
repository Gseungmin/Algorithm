import sys
input = sys.stdin.readline

C, N = map(int,input().split())
city = [list(map(int,input().split())) for i in range(N)]

M = C+101
INF = int(1e9)
dp = [[INF]*(M) for i in range(C)]
Ans = INF
for i in range(N):
    cost, num = city[i]
    dp[0][num] = min(dp[0][num], cost)
    if num >= C:
        Ans = min(Ans, cost)
    
for i in range(C-1):
    for j in range(M):
        if dp[i][j] != INF:
            for k in range(N):
                cost, num = city[k]
                if j+num < M:
                    dp[i+1][j+num] = min(dp[i+1][j+num], dp[i][j]+cost)
                    if j+num >= C:
                        Ans = min(Ans, dp[i+1][j+num])

print(Ans)
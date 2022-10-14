import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
INF = int(1e9)
dp = [[[-INF]*4 for i in range(M)] for j in range(N)]
dp[0][0][1] = graph[0][0]
dp[0][0][2] = graph[0][0]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        if j-1 >= 0 and dp[i][j-1][1] != -INF:
            dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][1]+graph[i][j])
        if j-1 >= 0 and dp[i][j-1][2] != -INF:
            dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][2]+graph[i][j])
        if i-1 >= 0 and dp[i-1][j][1] != -INF:
            dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][1]+graph[i][j])
        if i-1 >= 0 and dp[i-1][j][2] != -INF:
            dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][2]+graph[i][j])
        if i-1 >= 0 and dp[i-1][j][3] != -INF:
            dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][3]+graph[i][j])
        if j+1 < M and dp[i][j+1][3] != -INF:
            dp[i][j][3] = max(dp[i][j][3], dp[i][j+1][3]+graph[i][j])
        if j+1 < M and dp[i][j+1][2] != -INF:
            dp[i][j][3] = max(dp[i][j][3], dp[i][j+1][2]+graph[i][j])
    if i == 0:
        continue
    for j in range(M-1,-1,-1):
        if i == 0 and j == 0:
            continue
        if j-1 >= 0 and dp[i][j-1][1] != -INF:
            dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][1]+graph[i][j])
        if j-1 >= 0 and dp[i][j-1][2] != -INF:
            dp[i][j][1] = max(dp[i][j][1], dp[i][j-1][2]+graph[i][j])
        if i-1 >= 0 and dp[i-1][j][1] != -INF:
            dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][1]+graph[i][j])
        if i-1 >= 0 and dp[i-1][j][2] != -INF:
            dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][2]+graph[i][j])
        if i-1 >= 0 and dp[i-1][j][3] != -INF:
            dp[i][j][2] = max(dp[i][j][2], dp[i-1][j][3]+graph[i][j])
        if j+1 < M and dp[i][j+1][3] != -INF:
            dp[i][j][3] = max(dp[i][j][3], dp[i][j+1][3]+graph[i][j])
        if j+1 < M and dp[i][j+1][2] != -INF:
            dp[i][j][3] = max(dp[i][j][3], dp[i][j+1][2]+graph[i][j])
print(max(dp[N-1][M-1]))
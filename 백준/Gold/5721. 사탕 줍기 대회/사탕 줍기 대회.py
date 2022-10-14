import sys
input = sys.stdin.readline
while 1:
    N, M = map(int,input().split())
    if N == 0 and M == 0:
        break
    graph = [list(map(int,input().split())) for i in range(N)]
    dp = [[[0]*2 for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if j == 0:
                dp[i][j][1] = graph[i][j]
            else:
                dp[i][j][1] = graph[i][j] + dp[i][j-1][0]
                dp[i][j][0] = max(dp[i][j-1][0], dp[i][j-1][1])
    dp2 = [[0]*2 for i in range(N)]
    for i in range(N):
        if i == 0:
            dp2[i][1] = max(dp[i][M-1][1], dp[i][M-1][0])
        else:
            dp2[i][0] = max(dp2[i-1][1], dp2[i-1][0]) #이전 행을 먹은 경우
            dp2[i][1] = dp2[i-1][0] + max(dp[i][M-1][1], dp[i][M-1][0]) #지금 행을 먹을 경우
    print(max(dp2[N-1]))
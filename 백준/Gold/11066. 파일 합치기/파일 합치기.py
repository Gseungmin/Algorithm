import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    graph = list(map(int,input().split()))
    dp = [[-1]*N for i in range(N)]
    Len = 2
    while Len <= N:
        for i in range(N-Len+1):
            j = i+Len-1
            if Len == 2:
                dp[i][j] = graph[i] + graph[j]
                continue
            total = sum(graph[i:j+1])
            dp[i][j] = dp[i+1][j]+total
            for k in range(i+1,j):
                if k == j-1:
                    dp[i][j] = min(dp[i][j], dp[i][k]+total)
                else:
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+total)
        Len += 1
    print(dp[0][N-1])
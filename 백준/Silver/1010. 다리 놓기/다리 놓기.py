import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    if N == M:
        print(1)
        continue
    dp = [[0]*M for i in range(N)]
    for i in range(M-N+1):
        dp[0][i] = 1
    for i in range(1,N):
        for j in range(i,M-N+i+1):
            for k in range(j):
                if dp[i-1][k] != 0:
                    dp[i][j] += dp[i-1][k]
    print(sum(dp[N-1]))
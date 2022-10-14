import sys
input = sys.stdin.readline
N, K = map(int,input().split())
dp = [[[[0]*(K+1) for b in range(N+1)] for a in range(N+1)] for i in range(N)]
dp[0][1][0][0] = "A"
dp[0][0][1][0] = "B"
dp[0][0][0][0] = "C"
for i in range(1,N):
    for a in range(N+1):
        for b in range(N+1):
            for k in range(K+1):
                if a-1 >= 0:
                    if dp[i-1][a-1][b][k] != 0:
                        dp[i][a][b][k] = dp[i-1][a-1][b][k] + "A"
                        if k == K and i == N-1:
                            print(dp[i][a][b][k])
                            sys.exit()
                if b-1 >= 0 and k-a>=0:
                    if dp[i-1][a][b-1][k-a] != 0:
                        dp[i][a][b][k] = dp[i-1][a][b-1][k-a]+"B"
                        if k == K and i == N-1:
                            print(dp[i][a][b][k])
                            sys.exit()
                if k-a-b>=0:
                    if dp[i-1][a][b][k-a-b] != 0:
                        dp[i][a][b][k] = dp[i-1][a][b][k-a-b]+"C"
                        if k == K and i == N-1:
                            print(dp[i][a][b][k])
                            sys.exit()
print(-1)
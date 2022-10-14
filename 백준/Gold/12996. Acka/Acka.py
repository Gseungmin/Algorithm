import sys
input = sys.stdin.readline
N, A, B, C = map(int,input().split())
dp = [[[[0]*(C+1) for i in range(B+1)] for j in range(A+1)] for k in range(N+1)]
dp[0][0][0][0] = 1
for i in range(1,N+1):
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if a-1 >= 0:
                    if dp[i-1][a-1][b][c] != 0:
                        if dp[i][a][b][c] == 0:
                            dp[i][a][b][c] = dp[i-1][a-1][b][c]
                        else:
                            dp[i][a][b][c] = (dp[i][a][b][c] + dp[i-1][a-1][b][c]) % 1000000007
                if b-1 >= 0:
                    if dp[i-1][a][b-1][c] != 0:
                        if dp[i][a][b][c] == 0:
                            dp[i][a][b][c] = dp[i-1][a][b-1][c]
                        else:
                            dp[i][a][b][c] = (dp[i][a][b][c] + dp[i-1][a][b-1][c]) % 1000000007
                if c-1 >= 0:
                    if dp[i-1][a][b][c-1] != 0:
                        if dp[i][a][b][c] == 0:
                            dp[i][a][b][c] = dp[i-1][a][b][c-1]
                        else:
                            dp[i][a][b][c] = (dp[i][a][b][c] + dp[i-1][a][b][c-1 ]) % 1000000007
                if a-1 >= 0 and b-1 >= 0:
                    if dp[i-1][a-1][b-1][c] != 0:
                        if dp[i][a][b][c] == 0:
                            dp[i][a][b][c] = dp[i-1][a-1][b-1][c]
                        else:
                            dp[i][a][b][c] = (dp[i][a][b][c] + dp[i-1][a-1][b-1][c]) % 1000000007
                if c-1 >= 0 and b-1 >= 0:
                    if dp[i-1][a][b-1][c-1] != 0:
                        if dp[i][a][b][c] == 0:
                            dp[i][a][b][c] = dp[i-1][a][b-1][c-1]
                        else:
                            dp[i][a][b][c] = (dp[i][a][b][c] + dp[i-1][a][b-1][c-1]) % 1000000007
                if a-1 >= 0 and c-1 >= 0:
                    if dp[i-1][a-1][b][c-1] != 0:
                        if dp[i][a][b][c] == 0:
                            dp[i][a][b][c] = dp[i-1][a-1][b][c-1]
                        else:
                            dp[i][a][b][c] = (dp[i][a][b][c] + dp[i-1][a-1][b][c-1]) % 1000000007
                if a-1 >= 0 and b-1 >= 0 and c-1 >= 0:
                    if dp[i-1][a-1][b-1][c-1] != 0:
                        if dp[i][a][b][c] == 0:
                            dp[i][a][b][c] = dp[i-1][a-1][b-1][c-1]
                        else:
                            dp[i][a][b][c] = (dp[i][a][b][c] + dp[i-1][a-1][b-1][c-1]) % 1000000007
print(dp[N][A][B][C]%1000000007)
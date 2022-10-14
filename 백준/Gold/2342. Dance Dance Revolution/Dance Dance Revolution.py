import sys
input = sys.stdin.readline
List = list(map(int,input().split()))
N = len(List)
INF = int(1e9)
dp = [[[INF]*5 for j in range(5)] for i in range(N-1)]
dp[0][0][List[0]] = 2
dp[0][List[0]][0] = 2
for i in range(N-2):
    for r in range(5):
        for l in range(5):
            if dp[i][r][l] != INF:
                nx = List[i+1]
                if l != nx:
                    if r == 0:
                        dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+2)
                    elif r == 1:
                        if nx == 3:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+4)
                        elif nx == 1:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+1)
                        else:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+3)
                    elif r == 2:
                        if nx == 4:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+4)
                        elif nx == 2:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+1)
                        else:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+3)
                    elif r == 3:
                        if nx == 1:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+4)
                        elif nx == 3:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+1)
                        else:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+3)
                    elif r == 4:
                        if nx == 2:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+4)
                        elif nx == 4:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+1)
                        else:
                            dp[i+1][nx][l] = min(dp[i+1][nx][l], dp[i][r][l]+3)
                if r != nx:
                    if l == 0:
                        dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+2)
                    elif l == 1:
                        if nx == 3:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+4)
                        elif nx == 1:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+1)
                        else:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+3)
                    elif l == 2:
                        if nx == 4:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+4)
                        elif nx == 2:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+1)
                        else:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+3)
                    elif l == 3:
                        if nx == 1:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+4)
                        elif nx == 3:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+1)
                        else:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+3)
                    elif l == 4:
                        if nx == 2:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+4)
                        elif nx == 4:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+1)
                        else:
                            dp[i+1][r][nx] = min(dp[i+1][r][nx], dp[i][r][l]+3)
ans = INF
for i in range(5):
    for j in range(5):
        if dp[N-2][i][j] != INF:
            ans = min(ans, dp[N-2][i][j])
print(ans)
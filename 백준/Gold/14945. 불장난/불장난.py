import sys
input = sys.stdin.readline
N = int(input())
mod = 10007
dp = [[[0]*100 for i in range(100)] for j in range(101)]
dp[2][0][1] = 1
dp[2][1][0] = 1
if N == 1:
    print(1)
    sys.exit()
elif N == 2:
    print(2)
    sys.exit()
for i in range(2,N):
    for x in range(i):
        for y in range(i):
            if dp[i][x][y] != 0:
                dp[i+1][x][y] += dp[i][x][y]
                if x < y:
                    if x+1 < y:
                        dp[i+1][x+1][y] += dp[i][x][y]
                        dp[i+1][x+1][y] %= mod
                    dp[i+1][x][y+1] += dp[i][x][y]
                    dp[i+1][x][y+1] %= mod
                elif x > y:
                    if y+1 < x:
                        dp[i+1][x][y+1] += dp[i][x][y]
                        dp[i+1][x][y+1] %= mod
                    dp[i+1][x+1][y] += dp[i][x][y]
                    dp[i+1][x+1][y] %= mod
                dp[i+1][x+1][y+1] += dp[i][x][y]
                dp[i+1][x+1][y+1] %= mod
Sum = 0
for i in range(N):
    for j in range(N):
        Sum += dp[N][i][j]
print(Sum%mod)
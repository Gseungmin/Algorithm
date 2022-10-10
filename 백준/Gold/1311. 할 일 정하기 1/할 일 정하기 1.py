import sys
input = sys.stdin.readline
N = int(input())
D = [list(map(int,input().split())) for i in range(N)]
dp = [[-1]*(1<<N) for i in range(N)]
INF = int(1e9)
def RC(x, bit):
    if bit == (1<<N)-1:
        return 0
    if dp[x][bit] != -1:
        return dp[x][bit]
    dp[x][bit] = INF
    for i in range(N):
        if bit&(1<<i):
            continue
        dp[x][bit] = min(dp[x][bit], RC(x+1,bit|(1<<i))+D[x][i])
    return dp[x][bit]
print(RC(0,0))
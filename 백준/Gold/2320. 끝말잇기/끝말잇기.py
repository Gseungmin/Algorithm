import sys
input = sys.stdin.readline
N = int(input())
List = [0] + [input().rstrip() for i in range(N)]

dp = [[0]*(1<<(N+1)) for i in range(N+1)]

def DP(x, bit):
    if dp[x][bit] != 0:
        return dp[x][bit]
    check = 0
    for nx in range(1,N+1):
        if x == 0:
            check = 1
            dp[x][bit] = max(dp[x][bit], DP(nx, bit|(1<<nx))+len(List[nx]))
        else:
            if (1<<nx)&bit > 0:
                continue
            if List[x][-1] != List[nx][0]:
                continue
            check = 1
            dp[x][bit] = max(dp[x][bit], DP(nx, bit|(1<<nx))+len(List[nx]))
    if check == 0:
        return 0
    return dp[x][bit]

print(DP(0,1))
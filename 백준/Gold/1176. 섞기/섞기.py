import sys
input = sys.stdin.readline
N, K = map(int,input().split())
height = [0] + [int(input()) for i in range(N)]

dp = [[0]*(N+1) for i in range(1<<(N+1))]

def DP(x,bit):
    if bit == ((1<<(N+1))-1):
        dp[bit][x] = 1
        return 1
    if dp[bit][x] != 0:
        return dp[bit][x]
    check = 0
    m = 0
    for nx in range(1,N+1):
        if (1<<nx)&bit > 0:
            continue
        if x != 0:
            if abs(height[x]-height[nx]) <= K:
                continue
        check = 1
        m += DP(nx,bit|(1<<nx))
    if check == 0:
        return 0
    dp[bit][x] = m
    return dp[bit][x]

print(DP(0,1))
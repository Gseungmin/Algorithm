import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
INF = int(1e8)
dp = [[INF]*(1<<N) for i in range(N+1)]

def func(x, bit):
    if bit == (1<<N)-1:
        return 0
    if dp[x][bit] != INF:
        return dp[x][bit]
    if bit != (1<<N)-2:
        for nx in range(1,N):
            if (1<<nx)&bit > 0 or graph[x][nx] == 0:
                continue
            dp[x][bit] = min(dp[x][bit], func(nx, bit|(1<<nx)) + graph[x][nx])
    else:
        if graph[x][0] != 0:
            dp[x][bit] = min(dp[x][bit], func(0, bit|1) + graph[x][0])
    return dp[x][bit]

k = func(0,0)
print(k)
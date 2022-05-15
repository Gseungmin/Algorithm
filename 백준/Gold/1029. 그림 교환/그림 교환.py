import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().strip())) for i in range(N)]
dp = [[[0]*10 for j in range(N)] for i in range(1<<N)]

def DP(x, k, cost, num):
    m = dp[x][k][cost]
    if m != 0:
        return m
    m = num
    for i in range(N):
        if (1<<i)&x > 0 or cost > graph[k][i]:
            continue
        m = max(m,DP((1<<i)|x,i,graph[k][i],num+1))
    dp[x][k][cost] = m
    return m

print(DP(1,0,0,1))
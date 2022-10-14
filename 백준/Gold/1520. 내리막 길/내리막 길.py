import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
dp = [[-1]*M for i in range(N)]
dp[0][0] = 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def DP(x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if graph[nx][ny] > graph[x][y]:
                value += DP(nx,ny)
    dp[x][y] = value
    return value

print(DP(N-1,M-1))
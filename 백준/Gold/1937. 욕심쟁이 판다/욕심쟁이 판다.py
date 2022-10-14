import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]

dp = [[-1]*N for i in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = [1]
def DF(x,y):
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        value = 0
        if 0<=nx<N and 0<=ny<N:
            if graph[nx][ny] > graph[x][y]:
                k = DF(nx,ny)
                value += k
        if dp[x][y] < value+1:
            dp[x][y] = value+1
    ans[0] = max(ans[0], dp[x][y])
    return dp[x][y]

for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            DF(i,j)
print(ans[0])
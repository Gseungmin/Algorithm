import sys
input = sys.stdin.readline
N = int(input())
sx, sy = map(int,input().split())
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
INF = sys.maxsize
dp = [[INF]*5 for i in range(N+1)]
dp[0][0] = 0
Dict = dict()
Dict[(0,0)] = [sx,sy]
for i in range(1,N+1):
    x, y = map(int,input().split())
    for j in range(5):
        nx, ny = x+dx[j], y+dy[j]
        if 0<=nx<=100000 and 0<=ny<=100000:
            Dict[(i,j)] = [nx,ny]
for i in range(N):
    for j in range(5):
        if dp[i][j] != INF:
            x, y = Dict[(i,j)]
            for k in range(5):
                if (i+1,k) in Dict:
                    nx, ny = Dict[(i+1,k)]
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j]+abs(nx-x)+abs(ny-y))
print(min(dp[N]))
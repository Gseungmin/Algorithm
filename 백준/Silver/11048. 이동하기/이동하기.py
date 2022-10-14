import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(N)]
dp = [[-1]*M for i in range(N)]

dp[0][0] = graph[0][0]
dx = [1,0]
dy = [0,1]
def DP():
    for i in range(N):
        for j in range(M):
            for k in range(2):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<M:
                    dp[nx][ny] = max(dp[nx][ny], dp[i][j]+graph[nx][ny])
    return
DP()
print(dp[N-1][M-1])
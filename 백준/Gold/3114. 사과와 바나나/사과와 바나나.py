import sys
input = sys.stdin.readline
N, M = map(int,input().split())
graph = [list(map(str,input().split())) for i in range(N)]
apple = [[0]*M for i in range(N)]
banana = [[0]*M for i in range(N)]
for i in range(N):
    a_sum = 0
    b_sum = 0
    for j in range(M):
        if graph[i][j][0] == "A":
            a_sum += int(graph[i][j][1:])
        elif graph[i][j][0] == "B":
            b_sum += int(graph[i][j][1:])
        apple[i][j] = a_sum
        banana[i][j] = b_sum

dp = [[-1]*M for i in range(N)]
dp[0][0] = banana[0][M-1]-banana[0][0]
for x in range(N):
    for y in range(M):
        if dp[x][y] != -1:
            nx, ny = x, y+1
            if 0<=nx<N and 0<=ny<M:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y]-(banana[nx][ny]-banana[nx][y]))
            nx, ny = x+1, y
            if 0<=nx<N and 0<=ny<M:
                if ny == 0:
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y]+(banana[nx][M-1]-banana[nx][ny]))
                else:
                    dp[nx][ny] = max(dp[nx][ny], dp[x][y]+apple[nx][ny-1]+(banana[nx][M-1]-banana[nx][ny]))
            nx, ny = x+1, y+1
            if 0<=nx<N and 0<=ny<M:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y]+apple[nx][ny-1]+(banana[nx][M-1]-banana[nx][ny]))
print(dp[N-1][M-1])
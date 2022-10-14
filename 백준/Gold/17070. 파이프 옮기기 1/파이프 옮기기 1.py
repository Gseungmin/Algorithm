import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
memo = [[[0]*3 for i in range(N)] for j in range(N)]
for i in range(1, N):
    if graph[0][i] == 1:
        break
    memo[0][i][0] = 1

def DP(N, memo, graph):
    for i in range(1,N):
        for j in range(N):
            if graph[i][j] == 1:
                continue
            if j-1 >= 0:
                memo[i][j][0] = memo[i][j-1][0] + memo[i][j-1][1]
                if graph[i-1][j] == 0 and graph[i-1][j-1] == 0 and graph[i][j-1] == 0:
                    memo[i][j][1] = memo[i-1][j-1][0] + memo[i-1][j-1][1] + memo[i-1][j-1][2]
            memo[i][j][2] = memo[i-1][j][1] + memo[i-1][j][2]
    return

DP(N, memo, graph)
print(sum(memo[N-1][N-1]))
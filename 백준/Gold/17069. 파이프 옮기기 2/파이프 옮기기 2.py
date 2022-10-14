import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
memo = [[[0]*3 for i in range(N)] for i in range(N)]
memo[0][1][0] = 1

def DP(N, graph, memo):
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                continue
            if i == 0:
                if j == 0 or j == 1:
                    continue
            if j-1>=0:
                memo[i][j][0] = memo[i][j-1][2] + memo[i][j-1][0]
            if i-1>=0:
                memo[i][j][1] = memo[i-1][j][2] + memo[i-1][j][1]
            if j-1>=0 and i-1>=0:
                if graph[i-1][j] != 1 and graph[i][j-1] != 1:
                    memo[i][j][2] = memo[i-1][j-1][0] + memo[i-1][j-1][1] + memo[i-1][j-1][2] 
    print(sum(memo[N-1][N-1]))
    return

DP(N, graph, memo)
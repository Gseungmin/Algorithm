import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for i in range(N)]
memo = [[0]*N for i in range(N)]
memo[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        if memo[i][j] != 0:
            if j + graph[i][j] < N:
                memo[i][j+graph[i][j]] += memo[i][j]
            if i + graph[i][j] < N:
                memo[i+graph[i][j]][j] += memo[i][j]
            

print(memo[N-1][N-1])
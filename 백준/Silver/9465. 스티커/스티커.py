import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    memo = [[0]*(N)] + [list(map(int,input().split())) for j in range(2)]
    for j in range(1,N):
        memo[0][j] = max(memo[1][j-1], memo[2][j-1])
        memo[1][j] = max(memo[0][j-1] + memo[1][j], memo[2][j-1] + memo[1][j])
        memo[2][j] = max(memo[0][j-1] + memo[2][j], memo[1][j-1] + memo[2][j])
    print(max(memo[0][N-1], memo[1][N-1], memo[2][N-1]))
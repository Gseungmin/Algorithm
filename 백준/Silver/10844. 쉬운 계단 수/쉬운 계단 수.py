import sys #for using sys
input = sys.stdin.readline
N = int(input()) #num of step
memo = []
memo.append([0,0,0,0,0,0,0,0,0,0])
memo.append([1,1,1,1,1,1,1,1,1,1])
mod = 1000000000
for i in range(N-1):
    memo.append([0,0,0,0,0,0,0,0,0,0])
for i in range(2,N+1):
    memo[i][0] = memo[i-1][1] % mod
    memo[i][9] = memo[i-1][8] % mod
    for j in range(1,9):
        memo[i][j] = (memo[i-1][j-1] + memo[i-1][j+1]) % mod
print((sum(memo[N])-memo[N][0]) % mod)
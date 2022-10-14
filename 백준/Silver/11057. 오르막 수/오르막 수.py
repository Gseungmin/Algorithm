import sys
input = sys.stdin.readline
N = int(input())
memo = []
for i in range(N+1):
    memo.append([0]*10)
for i in range(10):
    memo[1][i] = 1
for i in range(2,N+1):
    for j in range(10):
        for k in range(j+1):
            memo[i][j] = (memo[i][j] + memo[i-1][k])%10007
print(sum(memo[N])%10007)
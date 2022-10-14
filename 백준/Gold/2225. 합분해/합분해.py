import sys
input = sys.stdin.readline
n, k = map(int,input().split())
memo = [[0]*(k+1) for i in range(n+1)]
for i in range(n+1):
    memo[i][1] = 1
for m in range(2,k+1):
    for i in range(n+1):
        for j in range(i+1):
            memo[i][m] += (memo[j][m-1])
print(memo[n][k]%1000000000)
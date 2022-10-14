import sys
input = sys.stdin.readline
t = int(input())
memo = [[0]*4 for i in range(100001)]
memo[1][1] = 1
memo[2][2] = 1
memo[3][3] = 1
memo[3][1] = 1
memo[3][2] = 1
for i in range(4, 100001):
    memo[i][1] = (memo[i-1][2] + memo[i-1][3])%1000000009
    memo[i][2] = (memo[i-2][1] + memo[i-2][3])%1000000009
    memo[i][3] = (memo[i-3][1] + memo[i-3][2])%1000000009
        
for _ in range(t):
    n = int(input())
    print(sum(memo[n])%1000000009)
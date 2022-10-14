import sys
input = sys.stdin.readline
N = int(input())
memo = [[0,0,0]]
memo.append([1,1,1])
for i in range(N-1):
    memo.append([0,0,0])
for i in range(2,N+1):
    memo[i][0] = (memo[i-1][0] + memo[i-1][1] + memo[i-1][2])%9901
    memo[i][1] = (memo[i-1][0] + memo[i-1][2])%9901
    memo[i][2] = (memo[i-1][0] + memo[i-1][1])%9901
print(sum(memo[N])%9901)
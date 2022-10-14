import sys #for using sys
input = sys.stdin.readline
N = int(input()) #num of step
memo = []
for i in range(N+1):
    memo.append([0,0])
memo[1][0] = 1
memo[1][1] = 1
for j in range(2,N+1):
    memo[j][1] = memo[j-1][0]
    memo[j][0] = memo[j-1][1] + memo[j-1][0]
print(memo[N][1])
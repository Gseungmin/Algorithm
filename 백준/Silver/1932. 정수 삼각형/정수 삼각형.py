import sys
input = sys.stdin.readline
N = int(input())
memo = []
for i in range(N):
    memo.append([0]*(i+1))
num = []
for i in range(N):
    num.append(list(map(int,input().split())))
memo[0][0] = num[0][0]
for i in range(1,N):
    for j in range(i+1):
        if j == 0:
            memo[i][j] = memo[i-1][j] + num[i][j]
        elif j == i:
            memo[i][j] = memo[i-1][j-1] + num[i][j]
        else:
            memo[i][j] = max(memo[i-1][j-1] + num[i][j], memo[i-1][j] + num[i][j])
print(max(memo[N-1]))
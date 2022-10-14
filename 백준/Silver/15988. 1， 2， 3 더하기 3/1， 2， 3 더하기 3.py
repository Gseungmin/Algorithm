import sys
input = sys.stdin.readline
T = int(input())
memo = [0] * (1000001)
memo[0] = 1
memo[1] = 1
memo[2] = 2
for i in range(3, 1000001):
    memo[i] = (memo[i-1] + memo[i-2] + memo[i-3]) % 1000000009
for k in range(T):
    N = int(input())
    print(memo[N]%1000000009)
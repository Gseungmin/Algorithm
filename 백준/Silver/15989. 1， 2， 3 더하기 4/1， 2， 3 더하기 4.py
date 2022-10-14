import sys
input = sys.stdin.readline
dp = [0]*10001
dp[0] = 1
for j in range(1,4):
    for i in range(1,10001):
        if i-j >= 0:
            dp[i] += dp[i-j]
    
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
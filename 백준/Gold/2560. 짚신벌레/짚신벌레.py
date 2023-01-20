import sys
input = sys.stdin.readline
a, b, d, N = map(int,input().split())

birth = [0]*(N+1)
birth[0] = 1
index = a
Sum = 0
for i in range(a,N+1):
    Sum += birth[i-a]
    if i-b < 0:
        birth[i] = Sum
        continue
    else:
        Sum -= birth[i-b]
        birth[i] = Sum
    birth[i] %= 1000
 
dp = [0]*(N+1)
for i in range(N+1):
    dp[i] = dp[i-1] + birth[i]
    if i-d >= 0:
        dp[i] -= birth[i-d]
    dp[i] %= 1000

print(dp[-1])
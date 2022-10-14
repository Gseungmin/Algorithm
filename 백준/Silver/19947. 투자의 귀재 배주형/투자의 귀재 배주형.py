import sys
input = sys.stdin.readline
H, Y = map(int,input().split())
dp = [0]*(Y+1)
dp[0] = H
for i in range(Y+1):
    if i+1 <= Y:
        dp[i+1] = max(dp[i+1],dp[i]+(dp[i]*5)//100)
    if i+3 <= Y:
        dp[i+3] = max(dp[i+3],dp[i]+(dp[i]*20)//100)
    if i+5 <= Y:
        dp[i+5] = max(dp[i+5],dp[i]+(dp[i]*35)//100)
print(dp[Y])
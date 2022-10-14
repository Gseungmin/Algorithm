import sys
input = sys.stdin.readline
dp = [0]*(10001)
dp[2] = 1
dp[4] = 2
Mod = 987654321
for i in range(6,10001,2):
    dp[i] = 2*dp[i-2]
    for j in range(2,i,2):
        if j > i-2-j:
            break
        if j == i-2-j:
            dp[i] += (dp[j]*dp[i-2-j])
            break
        else:
            dp[i] += (dp[j]*dp[i-2-j])*2
    dp[i] %= Mod
N = int(input())
print(dp[N])
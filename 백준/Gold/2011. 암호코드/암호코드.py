N = input()
if len(N) == 0:
    print(0)
    exit()
dp = [0]*len(N)
if N[0] == "0":
    print(0)
    exit()
if len(N) == 1:
    print(1)
    exit()
dp[0] = 1
K = len(N)
for i in range(1,K):
    if N[i] == "0":
        if  0 < int(N[i-1:i+1]) <= 26:
            if i-2 >= 0:
                dp[i] = (dp[i]+dp[i-2]) % 1000000
            else:
                dp[i] = (dp[i]+1) % 1000000
    else:
        dp[i] = (dp[i]+dp[i-1]) % 1000000
        if 0 < int(N[i-1:i+1]) <= 26 and N[i-1] != "0":
            if i-2 >= 0:
                dp[i] = (dp[i]+dp[i-2]) % 1000000
            else:
                dp[i] = (dp[i]+1) % 1000000
print(dp[K-1]%1000000)
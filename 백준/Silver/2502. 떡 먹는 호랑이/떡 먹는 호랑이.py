import sys
input = sys.stdin.readline
D, K = map(int,input().split())
for i in range(1,K):
    for j in range(i+1,K+1):
        dp = [0]*(D)
        dp[0] = i
        dp[1] = j
        for k in range(2,D):
            dp[k] = dp[k-1]+dp[k-2]
        if dp[D-1] == K:
            print(i)
            print(j)
            sys.exit()
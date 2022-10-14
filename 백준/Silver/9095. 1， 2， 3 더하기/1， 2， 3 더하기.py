import sys
input = sys.stdin.readline
T = int(input()) #testcase
for k in range(T):
    N = int(input())
    if N == 1 or N == 2:
        print(N)
    else:
        memo = [0] * (N+1)
        memo[1] = 1 #basecase
        memo[2] = 2 #basecase
        memo[3] = 4 #basecase
        for i in range(4, N+1): #by using memoization
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        print(memo[N])

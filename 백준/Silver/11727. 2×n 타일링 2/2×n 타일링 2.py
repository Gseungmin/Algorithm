import sys
input = sys.stdin.readline
N = int(input())
if N == 1:
    print(1)
else:
    memo = [0] * (N+1)
    memo[1] = 1 #basecase
    memo[2] = 3 #basecase
    for i in range(3,N+1): #by using memoization
        memo[i] = memo[i-1] + 2*memo[i-2]
    print(memo[N]%10007)

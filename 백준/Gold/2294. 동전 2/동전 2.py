import sys
input = sys.stdin.readline
N, K = map(int,input().split())
coin = [int(input()) for i in range(N)]
memo = [-1]*(K+1)
for i in coin:
    if i <= K:
        memo[i] = 1
for i in range(1,K+1):
    for j in range(N):
        if i-coin[j] >= 0:
            if memo[i-coin[j]] == -1:
                continue
            if memo[i] == -1:
                memo[i] = memo[i-coin[j]]+1
            else:
                memo[i] = min(memo[i], memo[i-coin[j]]+1)
print(memo[K])
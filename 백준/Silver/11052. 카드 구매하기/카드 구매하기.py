import sys
input = sys.stdin.readline
N = int(input())
memo = [0] + list(map(int,input().split()))
for i in range(1,N+1):
    for j in range((i//2)+1):
        memo[i] = max(memo[i], memo[i-j] + memo[j])
print(memo[N])
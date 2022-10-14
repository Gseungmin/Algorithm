import sys
input = sys.stdin.readline
N, K = map(int,input().split())
arr = list(map(int,input().split()))
dp = [0]*(N+1)

left, right, Sum = 0,0,0
while right <= N:
    if Sum >= K:
        while Sum >= K:
            dp[right] = max(dp[right], dp[left]+Sum-K)
            Sum -= arr[left]
            left += 1
    else:
        dp[right] = max(dp[right], dp[right-1])
        if right == N:
            break
        Sum += arr[right]
        right += 1
print(dp[N])
import sys
input = sys.stdin.readline
N, K = map(int,input().split())
List = list(map(int,input().split()))
Sum = [0]*N
Sum[0] = List[0]
for i in range(1,N):
    Sum[i] = Sum[i-1] + List[i]
dp = [0]*N
i = 0
j = 0
while i <= j < N:
    if i == 0:
        m = Sum[j]
    else:
        m = Sum[j]-Sum[i-1]
    if m >= K:
        if i == 0:
            dp[j] = m-K
        else:
            dp[j] = max(dp[j], max(dp[:i])+m-K)
        i += 1
        j = max(i,j)
    else:
        j += 1
print(dp[-1])
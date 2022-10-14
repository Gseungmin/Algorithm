import sys
input = sys.stdin.readline
Str = input().strip()
N = len(Str)
if N == 1:
    print(1)
    exit()
dp = [[False]*N for i in range(N)]
for i in range(N):
    dp[i][i] = True
for i in range(N-1):
    if Str[i] == Str[i+1]:
        dp[i][i+1] = True
Len = 3
while Len <= N:
    for i in range(N):
        if i+Len-1 >= N:
            break
        if Str[i] == Str[i+Len-1] and dp[i+1][i+Len-2] == True:
            dp[i][i+Len-1] = True
    Len += 1

ans = [int(1e9)]*N
for i in range(N):
    if i == 0:
        ans[i] = 1
    else:
        ans[i] = min(ans[i], ans[i-1]+1)
    for j in range(i+1,N):
        if dp[i][j] == True:
            if i == 0:
                ans[j] =  min(ans[j], 1)
            else:
                ans[j] =  min(ans[j], ans[i-1]+1)
print(ans[N-1])
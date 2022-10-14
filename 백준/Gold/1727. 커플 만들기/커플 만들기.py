import sys
input = sys.stdin.readline
N, M = map(int,input().split())
l1 = [0] + list(map(int,input().split()))
l2 = [0] + list(map(int,input().split()))
l1.sort()
l2.sort()
dif = dict()
dif[(0,0)] = 0
if N < M:
    l1, l2 = l2, l1
    N, M = M, N
for i in range(1,M+1):
    for j in range(1,N+1):
        dif[(i,j)] = abs(l1[j]-l2[i])

INF = int(1e9)
dp = [[INF]*(N+1) for i in range(M+1)]
def DP(m,n):
    if m == M:
        dp[m][n] = dif[(m,n)]
        return dif[(m,n)]
    if dp[m][n] != INF:
        return dp[m][n]
    k = INF
    for i in range(n+1,N+1):
        if N-i >= M-m-1:
            dp[m][n] = min(dp[m][n], DP(m+1, i)+dif[(m,n)])
    return dp[m][n]
    
print(DP(0,0))
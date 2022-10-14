import sys
input = sys.stdin.readline
C, E, D = map(int,input().split())
N = int(input())
S = [0] + list(map(int,input().split()))
S.append(D-sum(S))
A = [0] + list(map(int,input().split()))
INF = sys.maxsize
dp = [[INF]*(C+1) for i in range(N+2)]
dp[0][C] = 0
for i in range(1,N+2):
    for k in range(C+1):
        x = S[i]*E
        if k+x <= C:
            if dp[i-1][k+x] != INF:
                if i != N+1:
                    for j in range(C+1): #몇 리터를 넣을 것인가?
                        if k+j > C:
                            break
                        dp[i][k+j] = min(dp[i][k+j], dp[i-1][k+x]+A[i]*j)
                elif i == N+1:
                    dp[i][k] = min(dp[i][k], dp[i-1][k+x])
if min(dp[N+1]) == INF:
    print(-1)
else:
    print(min(dp[N+1]))
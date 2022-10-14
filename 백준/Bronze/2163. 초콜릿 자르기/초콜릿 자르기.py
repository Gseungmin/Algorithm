import sys
input = sys.stdin.readline
N, M = map(int,input().split())
dp = [[-1]*(M+1) for i in range(N+1)]

def RC(N, M):
    if N == 1 and M == 1:
        return 0
    if dp[N][M] != -1:
        return dp[N][M]
    k = 0
    if N >= M:
        if N % 2 == 0:
            k = RC(N//2, M)+RC(N//2, M) + 1
        else:
            k = RC(N//2, M)+RC((N//2)+1, M) + 1
    if N < M:
        if M % 2 == 0:
            k = RC(N, M//2)+RC(N, M//2) + 1
        else:
            k = RC(N, M//2)+RC(N, M//2+1) + 1
    dp[N][M] = k
    return k
print(RC(N,M))
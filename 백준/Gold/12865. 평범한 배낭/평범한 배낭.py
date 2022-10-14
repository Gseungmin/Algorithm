import sys
input = sys.stdin.readline
N, limit = map(int,input().split())
memo = [[0]*(limit+1) for i in range(N)]
W = []
P = []
for i in range(N):
    w, p = map(int,input().split())
    W.append(w)
    P.append(p)
if N == 1:
    if W[0] <= limit:
        print(P[0])
    else:
        print(0)
    sys.exit()

memo[0][W[0]] = P[0]
for i in range(1,N):
    for j in range(1,limit+1):
        if j-W[i] >= 0:
            memo[i][j] = max(memo[i-1][j], memo[i-1][j-W[i]] + P[i])
        else:
            memo[i][j] = memo[i-1][j]
print(max(memo[N-1]))
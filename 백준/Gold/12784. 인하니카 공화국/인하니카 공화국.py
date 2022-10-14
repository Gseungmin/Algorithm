import sys
input = sys.stdin.readline

def DP(x, prev):
    check = 0
    for nx in tree[x]:
        if nx == prev:
            continue
        check = 1
        k = DP(nx, x)
        dp[x] += k
    if check == 0:
        dp[x] = cost[(x,prev)]
    else:
        if x != 1:
            dp[x] = min(dp[x], cost[(x,prev)])
    return dp[x]

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    if N == 1:
        print(0)
        continue
    tree = [[] for i in range(N+1)]
    cost = dict()
    for i in range(M):
        a, b, c = map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
        cost[(a,b)] = c
        cost[(b,a)] = c
    dp = [0]*(N+1)
    ans = DP(1,-1)
    print(ans)
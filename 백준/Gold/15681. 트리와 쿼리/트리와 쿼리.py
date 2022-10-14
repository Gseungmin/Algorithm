import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, R, Q = map(int,input().split())
tree = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [1]*(N+1)
def DF(x,px):
    if x != R and len(tree[x]) == 1:
        dp[x] = 1
        return dp[x]
    value = 0
    for nx in tree[x]:
        if nx == px:
            continue
        value += DF(nx,x)
    dp[x] += value
    return dp[x]
DF(R,-1)
for i in range(Q):
    print(dp[int(input())])
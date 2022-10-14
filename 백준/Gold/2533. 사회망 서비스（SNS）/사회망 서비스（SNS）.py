import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
if N <= 3:
    print(1)
    sys.exit()
tree = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dp = [[0]*2 for i in range(N+1)]

def DF(x,px):
    for nx in tree[x]:
        if nx == px:
            continue
        DF(nx,x)
    for nx in tree[x]:
        if nx == px:
            continue
        dp[x][0] += dp[nx][1]
        dp[x][1] += min(dp[nx][1],dp[nx][0])
    dp[x][1] += 1
    return

for i in range(1,N+1):
    if len(tree[i]) > 1:
        DF(i,-1)
        print(min(dp[i][0], dp[i][1]))
        sys.exit()
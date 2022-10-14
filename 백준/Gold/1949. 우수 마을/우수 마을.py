import sys
input = sys.stdin.readline
N = int(input())
sys.setrecursionlimit(10**6)
people = [0] + list(map(int,input().split()))
tree = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
if N <= 2:
    print(max(people))
    sys.exit()

def DF(x, px):
    if len(tree) == 1:
        dp[x][0] = 0
        dp[x][1] = people
        return
    for nx in tree[x]:
        if nx == px:
            continue
        DF(nx,x)
    k = 0
    for nx in tree[x]:
        if nx == px:
            continue
        dp[x][0] += max(dp[nx][0], dp[nx][1])
        k += dp[nx][0]
    dp[x][1] = k + people[x]
    return

ans = 0
dp = [[0]*2 for i in range(N+1)]
for i in range(1,N+1):
    if len(tree[i]) > 1:
        DF(i,-1)
        break
for i in range(1,N+1):
    for j in range(2):
        ans = max(ans, dp[i][j])
print(ans)
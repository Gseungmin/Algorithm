import sys
input = sys.stdin.readline
N = int(input())
W = [0] + list(map(int,input().split()))
tree = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

node = [[[] for j in range(2)] for i in range(N+1)]
dp = [[0]*2 for i in range(N+1)]
for i in range(1,N+1):
    dp[i][1] = W[i]
    node[i][1].append(i)
def Tree_dp(x, prev):
    check = 0
    for nx in tree[x]:
        if nx == prev:
            continue
        check = 1
        Tree_dp(nx,x)
        if dp[nx][0] > dp[nx][1]:
            dp[x][0] += dp[nx][0]
            node[x][0] += node[nx][0]
        elif dp[nx][0] < dp[nx][1]:
            dp[x][0] += dp[nx][1]
            node[x][0] += node[nx][1]
        elif dp[nx][0] == dp[nx][1]:
            dp[x][0] += dp[nx][0]
            if len(node[nx][0]) < len(node[nx][1]):
                node[x][0] += node[nx][1]
            else:
                node[x][0] += node[nx][0]
        dp[x][1] += dp[nx][0]
        node[x][1] += node[nx][0]
    return
Tree_dp(1,-1)
n1 = node[1][0]
n2 = node[1][1]
n1.sort()
n2.sort()
if max(dp[1][0], dp[1][1]) == 0:
    if len(n1) > len(n2):
        print(len(n1))
        print(" ".join(map(str,n1)))
    else:
        print(len(n2))
        print(" ".join(map(str,n2)))
else:
    if dp[1][0] > dp[1][1]:
        print(dp[1][0])
        print(" ".join(map(str,n1)))
    else:
        print(dp[1][1])
        print(" ".join(map(str,n2)))
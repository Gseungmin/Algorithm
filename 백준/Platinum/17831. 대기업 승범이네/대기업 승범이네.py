import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
tree = [[] for i in range(N+1)]
List = [0]*2 + list(map(int,input().split()))
for i in range(2,N+1):
    tree[List[i]].append(i)
value = [0] + list(map(int,input().split()))

dp = [[0]*2 for i in range(N+1)]

def DP(x, prev):
    k = 0
    t = 0
    Dict = dict()
    for nx in tree[x]:
        if len(tree[nx]) == 0:
            continue
        DP(nx, x)
        if dp[nx][0] >= dp[nx][1]:
            Dict[nx] = 0
        else:
            Dict[nx] = 1
        k += max(dp[nx][0],dp[nx][1])
        dp[x][0] += max(dp[nx][0], dp[nx][1])
    for nx in tree[x]:
        if len(tree[nx]) == 0: #만약 nx가 리프노드일 경우
            dp[x][1] = max(dp[x][1], value[x]*value[nx]+k)
            continue
        if Dict[nx] == 0: #만약 nx가 사수가 아니면
            dp[x][1] = max(dp[x][1], value[x]*value[nx]+k)
        elif Dict[nx] == 1: #만약 nx가 사수면
            dp[x][1] = max(dp[x][1], value[x]*value[nx]+k-dp[nx][1]+dp[nx][0])
    return

DP(1, -1)
print(max(dp[1]))
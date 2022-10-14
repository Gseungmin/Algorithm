import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, M = map(int,input().split())
List = list(map(int,input().split()))
tree = [[] for i in range(N+1)]
for i in range(1,N):
    tree[List[i]].append(i+1)
value = dict()
for i in range(M):
    a, b = map(int,input().split())
    if a not in value:
        value[a] = b
    else:
        value[a] += b
dp = [0]*(N+1)
def DP(x,k):
    if x in value:
        k += value[x]
    dp[x] = k
    for nx in tree[x]:
        DP(nx,k)
    return
DP(1,0)
print(" ".join(map(str,dp[1:])))
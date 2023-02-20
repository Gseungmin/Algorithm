import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

#tree 초기화
tree = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int,input().split())
    tree[a].append(b)

List = list(map(int,input().split()))

dp = [0]*N

def tree_dp(x):
    
    if len(tree[x]) == 0: #리프 노드면
        return List[x]
    
    k = List[x]
    for nx in tree[x]:
        a = tree_dp(nx)
        if a > 0:
            k += a
    dp[x] = k
    return k

tree_dp(0)

print(dp[0])
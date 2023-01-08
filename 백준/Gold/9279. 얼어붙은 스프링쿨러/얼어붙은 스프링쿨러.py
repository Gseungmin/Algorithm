import sys
input = sys.stdin.readline
while True:
    try:
        N, C = map(int,input().split())
        tree = [[] for i in range(N+1)]
        for i in range(N-1):
            x, y, k = map(int,input().split())
            tree[x].append([y,k])
            tree[y].append([x,k])
        
        INF = int(1e9)
        dp = [0]*(N+1)
        dp[C] = 0
        
        def tree_dp(px, x, C):
            value = 0
            for nx, k in tree[x]:
                if nx == px:
                    continue
                if len(tree[nx]) == 1: #Leaf Node
                    dp[x] += k
                else: #Not Leaf Node
                    dp[x] += min(tree_dp(x, nx, C), k)
            return dp[x]
        
        tree_dp(-1,C,C)
        print(dp[C])
    except:
        break
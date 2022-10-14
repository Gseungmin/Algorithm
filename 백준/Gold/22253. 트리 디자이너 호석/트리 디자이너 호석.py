import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
Mod = 1000000007
N = int(input())
List = [0] + list(map(int,input().split()))
graph = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def DP(x,prev):
    dp = [0]*10
    dp[List[x]] += 1
    for nx in graph[x]:
        if nx == prev:
            continue
        k = DP(nx,x)
        for i in range(10):
            dp[i] += k[i]
            if i >= List[x]:
                dp[List[x]] += k[i]
            dp[i] %= Mod
    return dp
dp = DP(1,-1)
print((sum(dp))%Mod)
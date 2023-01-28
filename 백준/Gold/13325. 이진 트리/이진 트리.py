import sys
input = sys.stdin.readline

k = int(input())

List = list(map(int,input().split()))

dist = dict()
connect = dict()

arr = [2**(i) for i in range(k)]

p = 0
index = 0
for i in arr:
    
    for j in range(i):
        p += 1
        
        lc = p*2
        rc = p*2+1
        connect[p] = [lc, rc]
        
        dist[(p,lc)] = List[index]
        index += 1
        dist[(p,rc)] = List[index]
        index += 1

ans = [0]
dp = [0]*(2**(k+1))

Sum = [0]

def tree_dp(x):
    
    left = connect[x][0]
    right = connect[x][1]
    
    if left not in connect: #리프 노드면
        dp[x] = max(dist[(x,left)], dist[(x,right)])
        ans[0] += abs(dist[(x,left)] - dist[(x,right)])
        
    else:
        left_dp = tree_dp(left) + dist[(x,left)]
        right_dp = tree_dp(right) + dist[(x,right)]
        
        dp[x] = max(left_dp, right_dp)
        
        ans[0] += abs(left_dp - right_dp)
    
    return dp[x]
    
tree_dp(1)

def Sums(x):
    
    left = connect[x][0]
    right = connect[x][1]
    
    if left not in connect: #리프 노드면
        Sum[0] += dp[x]*2
        return
        
    else:
        Sum[0] += (dp[x]-dp[left])
        Sum[0] += (dp[x]-dp[right])
        Sums(left)
        Sums(right)
    return

Sums(1)

print(Sum[0])
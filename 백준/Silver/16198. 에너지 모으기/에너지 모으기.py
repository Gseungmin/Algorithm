import sys
input = sys.stdin.readline
N = int(input())
W = list(map(int,input().split()))

def reculsive(N, W, Sum, ans):
    if len(W) == 2:
        ans.append(Sum)
        return
    for i in range(1, len(W)-1):
        Sum += W[i-1]*W[i+1]
        value = W.pop(i)
        reculsive(N, W, Sum, ans)
        W.insert(i, value)
        Sum -= W[i-1]*W[i+1]
    return

ans = []
reculsive(N, W, 0, ans)
print(max(ans))
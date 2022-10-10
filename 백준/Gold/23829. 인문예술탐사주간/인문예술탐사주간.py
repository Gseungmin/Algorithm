import sys
input = sys.stdin.readline
from bisect import bisect_left
N, Q = map(int,input().split())
tree = list(map(int,input().split()))
S = [0]*N
m = 0
tree.sort()
for i in range(N):
    m += tree[i]
    S[i] = m
for i in range(Q):
    k = int(input())
    left = bisect_left(tree,k)
    if left == 0:
        ans = S[-1]-(len(tree)*k)
    elif left == len(S):
        ans = (len(tree)*k)-S[-1]
    else:
        ans = ((left*k)-S[left-1])+(S[-1]-S[left-1]-(len(tree)-left)*k)
    print(ans)
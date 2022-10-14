import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int,input().split())
List = [0] + list(map(str,input().split()))

UF = [i for i in range(N+1)]
def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

def Union(x,y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    elif X > Y:
        UF[X] = Y
    elif X < Y:
        UF[Y] = X
    return

import heapq
heap = []
for i in range(M):
    a, b, c = map(int,input().split())
    if List[a] == List[b]:
        continue
    heapq.heappush(heap,[c,a,b])
cnt = 0
ans = 0
while heap:
    t, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y or Find(X) == Y or Find(Y) == X or Find(X) == Find(Y):
        continue
    Union(X, Y)
    ans += t
    cnt += 1
if cnt == N-1:
    print(ans)
else:
    print(-1)
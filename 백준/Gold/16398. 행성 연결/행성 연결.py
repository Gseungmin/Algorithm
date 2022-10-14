import sys
input = sys.stdin.readline
N = int(input())
dist = [list(map(int,input().split())) for i in range(N)]

UF = [i for i in range(N)]

def Union(x, y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    elif X > Y:
        UF[X] = Y
    elif Y > X:
        UF[Y] = X
    return

def Find(x):
    if UF[x] == x:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

import heapq
heap = []
for i in range(N-1):
    for j in range(i+1,N):
        heapq.heappush(heap,[dist[i][j],i,j])
ans = 0
while heap:
    t, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    ans += t
    Union(X,Y)
print(ans)
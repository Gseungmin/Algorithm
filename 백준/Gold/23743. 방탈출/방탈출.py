import sys
input = sys.stdin.readline

def Union(x, y):
    X = Find(x)
    Y = Find(y)
    if X == Y:
        return
    if X > Y:
        UF[X] = Y
    elif X < Y:
        UF[Y] = X
    return

def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

N, M = map(int,input().split())
import heapq
heap = []
for i in range(M):
    a, b, c = map(int,input().split())
    heapq.heappush(heap,[c,a,b])
cost = [0] + list(map(int,input().split()))
for i in range(1,N+1):
    heapq.heappush(heap,[cost[i],0,i])
UF = [i for i in range(N+1)]
ans = 0
while heap:
    t, x, y = heapq.heappop(heap)
    X = Find(x)
    Y = Find(y)
    if X == Y:
        continue
    Union(X,Y)
    ans += t
print(ans)
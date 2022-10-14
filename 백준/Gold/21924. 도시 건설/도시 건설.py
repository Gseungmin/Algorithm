import sys
input = sys.stdin.readline
N, M = map(int,input().split())
import heapq
heap = []
total = 0
for i in range(M):
    a, b, c = map(int,input().split())
    total += c
    heapq.heappush(heap,[c,a,b])

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
    elif Y > X:
        UF[Y] = X
    return

Sum = 0
K = 0
while heap:
    c, a, b = heapq.heappop(heap)
    x = Find(a)
    y = Find(b)
    if x == y:
        continue
    K += 1
    Sum += c
    Union(x,y)
if K != N-1:
    print(-1)
else:
    print(total-Sum)
import sys
input = sys.stdin.readline

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
    if X in power:
        UF[Y] = X
    elif Y in power:
        UF[X] = Y
    else:
        if X > Y:
            UF[X] = Y
        elif X < Y:
            UF[Y] = X
    return

N, M, K = map(int,input().split())
city = set()
for i in range(1,N+1):
    city.add(i)
power = set(map(int,input().split()))
import heapq
heap = []
for i in range(M):
    a, b, c = map(int,input().split())
    heapq.heappush(heap,[c,a,b])
ans = 0
UF = [i for i in range(N+1)]
while heap:
    c, a, b = heapq.heappop(heap)
    x = Find(a)
    y = Find(b)
    if x == y:
        continue
    if x in power and y in power:
        continue
    Union(x,y)
    ans += c
print(ans)
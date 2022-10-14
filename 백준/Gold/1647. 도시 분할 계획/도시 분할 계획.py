import sys
input = sys.stdin.readline
import heapq

def Find(x):
    if x == UF[x]:
        return x
    y = Find(UF[x])
    UF[x] = y
    return y

def Union(x,y):
    a = Find(x)
    b = Find(y)
    if a == b:
        return
    elif a < b:
        UF[b] = a
    elif a > b:
        UF[a] = b
    return

N, M = map(int,input().split())
UF = [i for i in range(N+1)]
heap = []
Max = 0
for i in range(M):
    a, b, c = map(int,input().split())
    heapq.heappush(heap, [c,a,b])

ans = 0
Max = 0
while heap:
    t, x, y = heapq.heappop(heap)
    if Find(x) == Find(y):
        continue
    Union(x,y)
    ans += t
    Max = max(Max, t)
print(ans-Max)